# Generated by Django 5.1.2 on 2024-12-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xtracareers', '0011_payment_invoice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='invoice_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
