from django.urls import path, include
from xtracareers import views

# app_name = 'xtracareers'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('details_services/<int:services_id>/', views.details_services, name='details_services'),
    path('payment_portal/', views.payment_portal, name='payment_portal'),
    path('razorpay_payment/', views.razorpay_payment, name='razorpay_payment'),  # Razorpay payment page
    # Success and Failure pages after payment attempt
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-failure/', views.payment_failure, name='payment_failure'),
]