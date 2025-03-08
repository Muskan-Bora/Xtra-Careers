from django.contrib import admin
from xtracareers.models import services, Payment, candidate_cv, faqs

# Register your models here.
admin.site.register(services)
admin.site.register(Payment)
admin.site.register(candidate_cv)
admin.site.register(faqs)