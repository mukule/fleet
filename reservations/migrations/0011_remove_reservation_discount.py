# Generated by Django 4.2.3 on 2023-07-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0010_reservation_add_tax_reservation_use_custom_rates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='discount',
        ),
    ]
