# Generated by Django 5.1.2 on 2024-11-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xtracareers', '0005_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='selected_services',
            field=models.CharField(choices=[('Resume & Cover Letter', 'Resume & Cover Letter'), ('ATS Optimization', 'ATS Optimization'), ('Personal Branding', 'Personal Branding'), ('Mock Interview & Guidance', 'Mock Interview & Guidance')], max_length=500),
        ),
    ]
