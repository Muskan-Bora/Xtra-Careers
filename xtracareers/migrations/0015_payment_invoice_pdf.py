# Generated by Django 5.1.2 on 2024-12-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xtracareers', '0014_remove_payment_invoice_url_payment_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='invoice_pdf',
            field=models.FileField(blank=True, null=True, upload_to='invoices/'),
        ),
    ]
