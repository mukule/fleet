# Generated by Django 4.2.3 on 2023-08-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0036_income_carout_invoice_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='number_plate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
