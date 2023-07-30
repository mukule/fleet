# Generated by Django 4.2.3 on 2023-07-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_reservation_vat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='vat',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
