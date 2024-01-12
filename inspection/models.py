
from django.db import models
from django.core.validators import MaxValueValidator
from jsignature.fields import JSignatureField
from car.models import *


# Create your models here.


class EmergencyEquipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FluidStatusChoice(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class YesNoChoice(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class DamageImage(models.Model):
    inspection = models.ForeignKey(
        'Inspection', on_delete=models.CASCADE, related_name='damage_images')
    d_image = models.ImageField(upload_to='damage_images/')

    def __str__(self):
        return f"Damage Image for Inspection {self.inspection} ({self.id})"


class Inspection(models.Model):
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    current_mileage = models.PositiveIntegerField(
        validators=[MaxValueValidator(999999)])
    service_tag = models.CharField(max_length=100)
    next_service_due = models.CharField(max_length=100)
    insurance_expiry = models.DateField()
    fuel_tank_level = models.DecimalField(max_digits=5, decimal_places=2)
    emergency_equipment = models.ManyToManyField(
        EmergencyEquipment, blank=True)

    # ManyToManyField for fluid status choices
    oil_level = models.ManyToManyField(
        FluidStatusChoice, related_name='oil_level_inspections')
    brake_fluid = models.ManyToManyField(
        FluidStatusChoice, related_name='brake_fluid_inspections')
    power_steering_fluid = models.ManyToManyField(
        FluidStatusChoice, related_name='power_steering_fluid_inspections')
    clutch_fluid = models.ManyToManyField(
        FluidStatusChoice, related_name='clutch_fluid_inspections')
    auto_transmission_fluid = models.ManyToManyField(
        FluidStatusChoice, related_name='auto_transmission_fluid_inspections')
    radiator_fluid_level = models.ManyToManyField(
        FluidStatusChoice, related_name='radiator_fluid_level_inspections')
    windshield_washer_level = models.ManyToManyField(
        FluidStatusChoice, related_name='windshield_washer_level_inspections')

    voltage_recorded = models.DecimalField(max_digits=5, decimal_places=2)
    terminals_checked_and_tightened = models.ManyToManyField(
        YesNoChoice, related_name='terminals_checked_and_tightened_inspections')
    battery_fluid = models.ManyToManyField(
        YesNoChoice, related_name='battery_fluid_inspections')

    headlights_working = models.ManyToManyField(
        YesNoChoice, related_name='headlights_working_inspections')
    high_beam_working = models.ManyToManyField(
        YesNoChoice, related_name='high_beam_working_inspections')
    brake_lights_working = models.ManyToManyField(
        YesNoChoice, related_name='brake_lights_working_inspections')
    indicators_working = models.ManyToManyField(
        YesNoChoice, related_name='indicators_working_inspections')
    reverse_lights_working = models.ManyToManyField(
        YesNoChoice, related_name='reverse_lights_working_inspections')
    fog_lights_working = models.ManyToManyField(
        YesNoChoice, related_name='fog_lights_working_inspections')

    fr_tire_brand = models.CharField(max_length=100)
    fr_tire_condition = models.CharField(max_length=100)
    fl_tire_brand = models.CharField(max_length=100)
    fl_tire_condition = models.CharField(max_length=100)
    rr_tire_brand = models.CharField(max_length=100)
    rr_tire_condition = models.CharField(max_length=100)
    rl_tire_brand = models.CharField(max_length=100)
    rl_tire_condition = models.CharField(max_length=100)
    spare_tire_brand = models.CharField(max_length=100)
    spare_tire_condition = models.CharField(max_length=100)
    headlights_working = models.ManyToManyField(
        YesNoChoice, related_name='headlights_working_inspections')

    warning_lights = models.ManyToManyField(
        YesNoChoice, related_name='warning_lights_inspections')
    air_conditioning_working = models.ManyToManyField(
        YesNoChoice, related_name='air_conditioning_working_inspections')
    radio_working = models.ManyToManyField(
        YesNoChoice, related_name='radio_working_inspections')

    CD = models.ManyToManyField(YesNoChoice, related_name='CD_inspections')
    USB = models.ManyToManyField(YesNoChoice, related_name='USB_inspections')
    AUX = models.ManyToManyField(YesNoChoice, related_name='AUX_inspections')
    FM_Expander = models.ManyToManyField(
        YesNoChoice, related_name='FM_Expander_inspections')

    windscreen_condition = models.ManyToManyField(
        YesNoChoice, related_name='windscreen_condition_inspections')
    wipers_working = models.ManyToManyField(
        YesNoChoice, related_name='wipers_working_inspections')
    seat_belts_functioning = models.ManyToManyField(
        YesNoChoice, related_name='seat_belts_functioning_inspections')
    electric_mirrors_functioning = models.ManyToManyField(
        YesNoChoice, related_name='electric_mirrors_functioning_inspections')
    electric_windows_functioning = models.ManyToManyField(
        YesNoChoice, related_name='electric_windows_functioning_inspections')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    inspectors_first_name = models.CharField(max_length=50)
    inspectors_last_name = models.CharField(max_length=50)
    additional_comments = models.TextField(blank=True)
    dashboard_image = models.ImageField(
        upload_to='dashboard_images/', blank=True, null=True)
    car_damage_images =  models.ImageField(
        upload_to='dashboard_images/', blank=True, null=True)



    def __str__(self):
        return f"Inspection for {self.car} on {self.date}"
