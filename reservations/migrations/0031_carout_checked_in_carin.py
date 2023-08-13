# Generated by Django 4.2.3 on 2023-08-12 11:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0030_carout_created_at_carout_end_date_carout_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='carout',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='CarIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('seating_capacity', models.PositiveIntegerField()),
                ('car_class', models.CharField(max_length=100)),
                ('mileage', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999999)])),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('ld_appt_number', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('drivers_license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('country_of_issue', models.CharField(blank=True, max_length=50, null=True)),
                ('license_expiry', models.DateField(blank=True, null=True)),
                ('credit_card', models.CharField(blank=True, max_length=50, null=True)),
                ('credit_card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('card_expiry', models.DateField(blank=True, null=True)),
                ('physical_address', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('office_telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('residence_address', models.CharField(blank=True, max_length=100, null=True)),
                ('where_the_car_will_be_used_or_parked', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fuel_out', models.CharField(choices=[('1/4', '1/4'), ('1/2', '1/2'), ('3/4', '3/4'), ('Full', 'Full')], max_length=5, null=True)),
                ('fuel_in', models.CharField(choices=[('1/4', '1/4'), ('1/2', '1/2'), ('3/4', '3/4'), ('Full', 'Full')], max_length=5, null=True)),
                ('kms_out', models.PositiveIntegerField(blank=True, null=True)),
                ('kms_in', models.PositiveIntegerField(blank=True, null=True)),
                ('kms_driven', models.PositiveIntegerField(blank=True, null=True)),
                ('kms_allowed', models.PositiveIntegerField(blank=True, null=True)),
                ('damages_noted', models.TextField(blank=True, null=True)),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.paymentmethod')),
            ],
        ),
    ]
