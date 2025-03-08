from django.shortcuts import render, redirect
from django.http import JsonResponse
from xtracareers.models import services, Payment, faqs
from .forms import PaymentForm
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import timedelta, timezone, datetime 
import logging
import requests
import traceback
from time import sleep
from reportlab.pdfgen import canvas
from io import BytesIO
import io  # Import the io module
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# from weasyprint import HTML
from .utils import convert_to_words  # Utility function to convert number to words
from xhtml2pdf import pisa
from django.templatetags.static import static
from django.http import HttpResponse
import requests
from django.core.files.base import ContentFile
import ast

# from django.contrib import messages

# Create your views here.

def index(request):
    SERVICE = services.objects.all()
    FAQS = faqs.objects.all()
    
    context = {
        'SERVICE':SERVICE,
        'FAQS':FAQS,
    }

    return render(request, 'xtra_careers/index.html', context)

def details_services(request, services_id):
    
    detailservices = services.objects.get(id = services_id)
    
    context = {
        'detailservices':detailservices
    }
    
    return render(request, 'xtra_careers/details_services.html', context)

# ----------------------- Fresh ------------------------ 

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

def payment_portal(request):
    """Displays the payment form page."""
    if request.method == "POST":
        # Fetch form data from the POST request
        form = PaymentForm(request.POST)
        
        if form.is_valid():
            # Clean the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            experience_level = form.cleaned_data['experience_level']
            selected_services = form.cleaned_data['selected_services']
            final_amount = form.cleaned_data['amount']  # Amount is cleaned here
            print(f"Final amount: {final_amount}")  # Debugging line

            # Save payment details to the database
            payment = Payment.objects.create(
                name=name,
                email=email,
                contact=contact,
                experience_level=experience_level,
                selected_services=selected_services,
                amount=final_amount,
            )
            
            # Create Razorpay order data
            order_data = {
                'amount': int(final_amount) * 100,  # Convert to paise (Razorpay works with paise)
                'currency': 'INR',
                'payment_capture': '1',  # Auto-capture payment
            }
            
            # Create an order with Razorpay
            order = client.order.create(data=order_data)
            
            # Save Razorpay order id in the database
            payment.razorpay_order_id = order['id']
            payment.save()

            # Pass the order details to the payment template
            context = {
                'payment': payment,
                'order_id': order['id'],
                'amount': final_amount,
                'razorpay_key': settings.RAZORPAY_API_KEY  # Your Razorpay API Key
            }
            
            return render(request, 'xtra_careers/razorpay_payment.html', context)
        else:
            # If form is not valid, render the form with error messages
            return render(request, 'xtra_careers/payment_portal.html', {'form': form})

    else:
        # Instantiate an empty form when the page is loaded with GET request
        form = PaymentForm()

    return render(request, 'xtra_careers/payment_portal.html', {'form': form})

logger = logging.getLogger(__name__)

def payment_success(request):
    payment = Payment.objects.filter(payment_status="Success").latest('id')  # Fetch the latest successful payment
    return render(request, 'xtra_careers/payment_success.html', {'payment': payment})

# -----------------------------------------------------------------------

@csrf_exempt
def razorpay_payment(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        if not all([payment_id, order_id, signature]):
            logger.error("Missing required Razorpay parameters.")
            return JsonResponse({"error": "Missing Razorpay parameters"}, status=400)

        try:
            # Fetch the payment object
            payment = Payment.objects.get(razorpay_order_id=order_id)
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature

            # Verify the payment signature
            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            }
            client.utility.verify_payment_signature(params_dict)
            
            # Mark the payment as successful
            payment.payment_status = "Success"
            payment.save()
            
            # Send email with invoice
            send_payment_email(request, payment)

            return redirect('payment_success')

        except Payment.DoesNotExist:
            logger.error(f"Payment with Razorpay order ID {order_id} not found.")
            return JsonResponse({"error": "Payment not found"}, status=404)

        except razorpay.errors.SignatureVerificationError as e:
            logger.error(f"Signature verification failed: {e}")
            payment.payment_status = "Failed"
            payment.save()
            return JsonResponse({"error": f"Signature verification failed: {str(e)}"}, status=400)

        except Exception as e:
            logger.error(f"Error occurred during payment processing: {str(e)}")
            payment.payment_status = "Failed"
            payment.save()
            return redirect('payment_failure')

    return JsonResponse({"error": "Invalid request method"}, status=400)

def payment_failure(request):
    """Handle payment failure page."""
    return render(request, 'xtra_careers/payment_failure.html')

def generate_invoice(request, payment):
    """Generate the invoice PDF for a payment."""
    
    # Define rates for services based on experience levels
    # Example: Adjust rates for your actual logic
    service_rates = {
        'ATS Optimized Resume and Cover Letter': {
            '0-5': 1500,
            '6-10': 2000,
            '11-15': 3000,
            '15+': 4000,
        },
        
        'Personal Branding (LinkedIn)': {
            '0-5': 1000,
            '6-10': 1500,
            '11-15': 2000,
            '15+': 2500,
        },
        
        'Mock Interviews and Guidance': {
            '0-5': 1500,
            '6-10': 2500,
            '11-15': 5000,
            '15+': 10000,
        },
    }
    
    # Parse selected services and calculate amounts
    selected_services = payment.selected_services  # Assuming services are comma-separated
    experience_level = payment.experience_level.lower()  # Ensure experience level is lowercase
    items = []
    subtotal = 0
    
    for service in selected_services:
    # service = service.strip()  # Remove leading/trailing whitespace
        normalized_service = service.replace(" ", "").lower()  # Normalize spaces and case
        normalized_service_rates = {k.replace(" ", "").lower(): v for k, v in service_rates.items()}  # Normalize dictionary keys
        
        if normalized_service in normalized_service_rates:
            # Fetch the original service rates using the normalized key
            original_service = next(k for k in service_rates if k.replace(" ", "").lower() == normalized_service)
            rate = normalized_service_rates[normalized_service][experience_level]
            subtotal += rate  # Add to subtotal
            items.append({
                'name': original_service,  # Use the original service name
                'hsn_sac': '99851',
                'quantity': 1,
                'rate': rate,
                'paid_amount': rate,
            })
        else:
            print(f"Service '{service}' not found in service_rates")
    
     # Calculate discounts
    discount = 0
    if len(selected_services) == 2:  # 10% discount for 2 services
        discount = subtotal * 0.10
    elif len(selected_services) == len(service_rates):  # 20% discount for all services
        discount = subtotal * 0.20
    
    discounted_subtotal = subtotal - discount  # Apply the discount

    # Calculate GST
    gst_amount = discounted_subtotal * 0.18  # 18% GST

    # Calculate total amount (after GST)
    total_amount = discounted_subtotal + gst_amount

    # Paid amount (assuming payment.amount reflects actual paid amount)
    paid_amount = payment.amount
    amount_in_words = convert_to_words(total_amount)

    
    # Prepare context data for rendering
    context = {
        'company_name': 'Fluxwings Solutions LLP',
        'company_address': 'Office no 60, AWFIS, 18th floor, Cyber One, Sector 30 A, Vashi Navi Mumbai, Thane Maharashtra 400703 India',
        'comapany_email': 'director@fluxwings.com',
        'gstin_number': '27AAJFF4286A1ZI',
        'company_contact': '8308212194',
        'company_certificate': 'MSME/UDYAM NO.-UDYAM-MH-33-0516400',
        'invoice_number': f"AA/12/24/{payment.invoice_id}",
        'invoice_date': payment.payment_date.strftime('%d/%m/%Y'),
        'place_of_supply': 'Maharashtra (27)',
        'customer_name': payment.name,
        'customer_email': payment.email,
        'customer_contact': payment.contact,
        'items': items,
        'subtotal': subtotal,
        'discount': discount,
        'gst_amount': gst_amount,
        'total_amount': total_amount,
        'paid_amount': paid_amount,
        'amount_in_words': amount_in_words,
    }
    
    # Render the invoice template
    html_content = render_to_string('xtra_careers/invoice_template.html', context)
    
    # Convert HTML to PDF
    pdf_file = io.BytesIO()
    pisa.CreatePDF(html_content, dest=pdf_file)
    pdf_file.seek(0)  # Reset the pointer to the start of the buffer
    
    return pdf_file
    
def send_payment_email(request, payment):
    """Send email with the invoice after successful payment."""

    # Ensure invoice ID is generated
    if not payment.invoice_id:
        payment.invoice_id = f"INV-{payment.id:05d}-{datetime.now().strftime('%Y%m%d')}"
        payment.save()

    # Generate the invoice PDF
    pdf_buffer = generate_invoice(request, payment)

    # Save the PDF to the database
    pdf_filename = f"Invoice_{payment.invoice_id}.pdf"
    payment.invoice_pdf.save(pdf_filename, ContentFile(pdf_buffer.getvalue()))

    # Fetch further proceedings based on selected services
    further_proceedings = []

    # Parse selected services (assuming it's stored as a stringified list or comma-separated string)
    try:
        selected_services = ast.literal_eval(payment.selected_services)  # Parse list of IDs/names
    except (ValueError, SyntaxError):
        selected_services = payment.selected_services  # Fallback for comma-separated string
    print(f"Parsed selected services: {payment.selected_services}")

    # Clean and normalize selected services
    selected_services = [service.strip() for service in selected_services if service.strip()]

    # Fetch further details for each service
    for service_name in payment.selected_services:
        try:
            detailservices = services.objects.get(service_name__iexact=service_name)
            print(f"Service Found: {detailservices.service_name}, Further Details: {detailservices.further_detail_mail}")  # Debugging
            further_proceedings.append(f"{detailservices.service_name}: {detailservices.further_detail_mail}")
        except:
            print(f"Service Not Found: {service_name}")  # Debugging
            further_proceedings.append(f"{service_name}: Details not available.")

    # Subject and message body for the email
    subject = "Payment Successful - ExtraCareers"
    message = (
        f"Dear {payment.name},\n\n"
        f"Thank you for choosing our services. Your payment of INR {payment.amount} "
        f"for the following services {(payment.selected_services)} has been successfully processed:\n\n"
        f"Please find the invoice attached.\n\n"
    )

    # Add further proceedings to the email
    if further_proceedings:
        message += "Further proceedings for your selected services:\n\n"
        message += "\n\n".join(further_proceedings)
        message += "\n\n"

    print(f"Further proceedings: {further_proceedings}")
    # Final message footer
    message += "Best regards,\nExtraCareers Team"

    # Prepare the email
    email = EmailMessage(
        subject,
        message,
        'director@fluxwings.com',  # Sender's email
        [payment.email],  # Recipient email
    )

    # Attach the invoice PDF with dynamic filename
    email.attach(f"Invoice_{payment.invoice_id}.pdf", pdf_buffer.read(), 'application/pdf')

    # Send the email
    email.send()

    # Update the invoice status to 'Success' in the database
    payment.invoice_status = 'Success'
    payment.save()

    # Log success or perform further actions after email is sent
    print(f"Invoice sent to {payment.email} for Invoice ID: {payment.invoice_id}")