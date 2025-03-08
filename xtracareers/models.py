from django.db import models

# Create your models here.

class services(models.Model):
    service_name = models.CharField(
        max_length = 100,
        default = 'service name'
    )
    
    service_icon = models.CharField(
        max_length = 100,
        default = 'fas fa-file-alt'
    )
    
    service_tagline = models.ImageField(
        upload_to = 'services_tagline',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    service_importance = models.TextField(
        default = 'Importance of Service'
    )
    
    service_mission = models.TextField(
        default = 'Mission'
    )
    
    service_valueproposition = models.ImageField(
        upload_to = 'services_valueproposition',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    service_mainheading = models.ImageField(
        upload_to = 'services_mainheading',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    service_introheading = models.CharField(
        max_length = 500,
        default = 'Intro Heading'
    )
    
    service_intro = models.TextField(
        default = 'Introduction'
    )
    
    service_whatweoffer_heading = models.CharField(
        max_length = 500,
        default = 'What we offer (Heading)'
    )
    
    service_whatweoffer_desc = models.TextField(
        default = 'What we offer (desc)'
    )
    
    service_whychoose_heading = models.CharField(
        max_length = 500,
        default = 'why choose (heading)'
    )
    
    service_whychoose_desc = models.TextField(
        default = 'why choose (desc)'
    )
    
    service_getstartedtoday_heading = models.CharField(
        max_length = 100,
        default = 'Get started today (heading)'
    )
    
    service_getstartedtoday_desc = models.TextField(
        default = 'Get started Today (Desc)'
    )
    
    service_quote = models.ImageField(
        upload_to = 'services_quote',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    service_thankyou = models.TextField(
        default = 'Thank You Message'
    )
    
    service_img1 = models.ImageField(
        upload_to = 'services',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    service_img2 = models.ImageField(
        upload_to = 'services',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    service_img3 = models.ImageField(
        upload_to = 'services',
        default = 'https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    pricing_junior = models.CharField(
        max_length = 100,
        default = 'Junior'
    )
    
    pricings_year = models.CharField(
        max_length = 50,
        default = 'no. of years'
    )
    
    pricing_juniorprice = models.CharField(
        max_length= 200,
        default = '100'
    )
    
    pricing_mid = models.CharField(
        max_length = 100,
        default = 'Mid'
    )
    
    pricing_no_year = models.CharField(
        max_length = 50,
        default = 'No. of years'
    )
    
    pricing_midprice = models.CharField(
        max_length= 200,
        default = '100'
    )
    
    pricing_senior = models.CharField(
        max_length = 100,
        default = 'senior'
    )
    
    pricing_year = models.CharField(
        max_length = 50,
        default = 'no of years'
    )
    
    pricing_seniorprice = models.CharField(
        max_length= 200,
        default = '100'
    )
    
    pricing_top = models.CharField(
        max_length = 100,
        default = 'Top'
    )
    
    pricing_n_years = models.CharField(
        max_length = 50,
        default = 'no of years'
    )
    
    pricing_topprice = models.CharField(
        max_length= 200,
        default = '100'
    )

    further_detail_mail = models.TextField(
        default='Further Detail of Services for Mail'
    )
    
    def __str__(self):
        return self.service_name
    
class Payment(models.Model) :
    EXPERIENECE_CHOICES = [
        ('0-5', '0 to 5 years'),
        ('6-10', '6 to 10 years'),
        ('11-15', '11 to 15 years'),
        ('15+', '15 years +'),
    ]
    
    SERVICES_CHOICES = [
        ('ATS Optimized Resume and Cover Letter', 'ATS Optimized Resume and Cover Letter'),
        # ('ATS Optimization', 'ATS Optimization'),
        ('Personal Branding (LinkedIn)', 'Personal Branding (LinkedIn)'),
        ('Mock Interviews and Guidance', 'Mock Interviews and Guidance'),
    ]
    
    name = models.CharField(
        max_length = 500,
        default= 'Customer Name'
    )
    
    email = models.EmailField()
    
    contact = models.CharField(max_length=15)
    
    experience_level = models.CharField(max_length= 10, choices= EXPERIENECE_CHOICES)
    
    selected_services = models.JSONField() 
    
    razorpay_order_id = models.CharField(max_length = 100, blank = True, null = True)
    
    razorpay_payment_id = models.CharField(max_length = 100, blank = True, null = True)
    
    razorpay_Signature = models.CharField(max_length = 255, blank = True, null = True)
    
    payment_status = models.CharField(max_length = 50, default = "Pending")
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    invoice_id = models.CharField(max_length=100, blank=True, null=True)
    
    payment_date = models.DateTimeField(auto_now_add=True)
    
    invoice_status = models.CharField(max_length=20, default="Pending")
    
    invoice_pdf = models.FileField(upload_to='invoices/', null=True, blank=True)  # Field to store PDF
    
    def __str__(self):
        return self.name
    

VETERAN_CHOICES = [
    ('Yes', 'Yes'),
    ('No','No'),
]

class candidate_cv(models.Model):
    cv_name = models.CharField(
        max_length=500,
        default="Name"
    )
    
    cv_contact = models.IntegerField(
        default="1234567890"
    )
    
    cv_email = models.EmailField(
        default="email@gmail.com"
    )
    
    key_skills = models.TextField(
        default="key skills"
    )
    
    cv_total_experience = models.IntegerField(
        default="1",
        null=True, blank=True
    )
    
    cv_undergraduate = models.TextField(
        default="undergraduate",
    )

    cv_postgraduate = models.TextField(
        default="postgraduate",
    )
    
    cv_certifications = models.TextField(
        blank=True
    )
    
    veteran_status = models.CharField(
        max_length=3, 
        choices = VETERAN_CHOICES
    )
    
    resumes = models.FileField(upload_to='resumes/')
    
    def __str__(self):
        return self.cv_name
    
class faqs (models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question