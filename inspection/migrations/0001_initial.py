# Generated by Django 4.2.3 on 2023-12-19 12:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0026_alter_carservice_next_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_image', models.ImageField(upload_to='damage_images/')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('current_mileage', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)])),
                ('service_tag', models.CharField(max_length=100)),
                ('next_service_due', models.DateField()),
                ('insurance_expiry', models.DateField()),
                ('fuel_tank_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('oil_level', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('brake_fluid', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('power_steering_fluid', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('clutch_fluid', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('auto_transmission_fluid', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('radiator_fluid_level', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('windshield_washer_level', models.IntegerField(choices=[(1, 'OK'), (2, 'Top Up'), (3, 'Check')])),
                ('voltage_recorded', models.DecimalField(decimal_places=2, max_digits=5)),
                ('terminals_checked_and_tightened', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('battery_fluid', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('high_beam_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('brake_lights_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('indicators_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('reverse_lights_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('fog_lights_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('fr_tire_brand', models.CharField(max_length=100)),
                ('fr_tire_condition', models.CharField(max_length=100)),
                ('fl_tire_brand', models.CharField(max_length=100)),
                ('fl_tire_condition', models.CharField(max_length=100)),
                ('rr_tire_brand', models.CharField(max_length=100)),
                ('rr_tire_condition', models.CharField(max_length=100)),
                ('rl_tire_brand', models.CharField(max_length=100)),
                ('rl_tire_condition', models.CharField(max_length=100)),
                ('spare_tire_brand', models.CharField(max_length=100)),
                ('spare_tire_condition', models.CharField(max_length=100)),
                ('headlights_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('warning_lights', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('air_conditioning_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('radio_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('CD', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('USB', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('AUX', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('FM_Expander', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('windscreen_condition', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('wipers_working', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('seat_belts_functioning', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('electric_mirrors_functioning', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('electric_windows_functioning', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('drivers_signature', jsignature.fields.JSignatureField()),
                ('inspectors_first_name', models.CharField(max_length=50)),
                ('inspectors_last_name', models.CharField(max_length=50)),
                ('inspectors_signature', jsignature.fields.JSignatureField()),
                ('additional_comments', models.TextField(blank=True)),
                ('dashboard_image', models.ImageField(blank=True, null=True, upload_to='dashboard_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('car_damage_images', models.ManyToManyField(blank=True, related_name='inspections', to='inspection.damageimage')),
                ('emergency_equipment', models.ManyToManyField(blank=True, to='inspection.emergencyequipment')),
            ],
        ),
        migrations.AddField(
            model_name='damageimage',
            name='inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damage_images', to='inspection.inspection'),
        ),
    ]
