# Generated by Django 4.2.3 on 2023-08-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0024_fuel_inspectionitemstatus_damages_noted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carout',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='carout',
            name='id_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]