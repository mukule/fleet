# Generated by Django 4.2.3 on 2023-07-25 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_reservation_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
