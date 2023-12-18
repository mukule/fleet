
from django.db import models
from django.core.validators import MaxValueValidator
from jsignature.fields import JSignatureField


# Create your models here.


class EmergencyEquipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class DamageImage(models.Model):
    inspection = models.ForeignKey('Inspection', on_delete=models.CASCADE, related_name='damage_images')
    image = models.ImageField(upload_to='damage_images/')

    def __str__(self):
        return f"Damage Image for Inspection {self.inspection} ({self.id})"


class Inspection(models.Model):
    FLUID_STATUS_CHOICES = [
        (1, 'OK'),
        (2, 'Top Up'),
        (3, 'Check'),
        
    ]

    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    date = models.DateField()
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    current_mileage = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    service_tag = models.CharField(max_length=100)
    next_service_due = models.DateField()
    insurance_expiry = models.DateField()
    fuel_tank_level = models.DecimalField(max_digits=5, decimal_places=2)
    emergency_equipment = models.ManyToManyField('EmergencyEquipment', blank=True)

    # Choice fields for fluid levels
    oil_level = models.IntegerField(choices=FLUID_STATUS_CHOICES)
    brake_fluid = models.IntegerField(choices=FLUID_STATUS_CHOICES)
    power_steering_fluid = models.IntegerField(choices=FLUID_STATUS_CHOICES)
    clutch_fluid = models.IntegerField(choices=FLUID_STATUS_CHOICES)
    auto_transmission_fluid = models.IntegerField(choices=FLUID_STATUS_CHOICES)
    radiator_fluid_level = models.IntegerField(choices=FLUID_STATUS_CHOICES)
    windshield_washer_level = models.IntegerField(choices=FLUID_STATUS_CHOICES)

    voltage_recorded = models.DecimalField(max_digits=5, decimal_places=2)
    terminals_checked_and_tightened = models.BooleanField(choices=YES_NO_CHOICES)
    battery_fluid = models.BooleanField(choices=YES_NO_CHOICES)

    headlights_working = models.BooleanField(choices=YES_NO_CHOICES)
    high_beam_working = models.BooleanField(choices=YES_NO_CHOICES)
    brake_lights_working = models.BooleanField(choices=YES_NO_CHOICES)
    indicators_working = models.BooleanField(choices=YES_NO_CHOICES)
    reverse_lights_working = models.BooleanField(choices=YES_NO_CHOICES)
    fog_lights_working = models.BooleanField(choices=YES_NO_CHOICES)

    fr_brand = models.CharField(max_length=100)
    fr_condition = models.CharField(max_length=100)
    fl_brand = models.CharField(max_length=100)
    fl_condition = models.CharField(max_length=100)
    rr_brand = models.CharField(max_length=100)
    rr = models.CharField(max_length=100)
    rl_brand = models.CharField(max_length=100)
    rl_condition = models.CharField(max_length=100)
    spare_brand = models.CharField(max_length=100)
    spare_condition = models.CharField(max_length=100)
    headlights_working = models.BooleanField(choices=YES_NO_CHOICES)

    warning_lights = models.BooleanField(choices=YES_NO_CHOICES)
    air_conditioning_working = models.BooleanField(choices=YES_NO_CHOICES)
    radio_working = models.BooleanField(choices=YES_NO_CHOICES)

    CD = models.BooleanField(choices=YES_NO_CHOICES)
    USB = models.BooleanField(choices=YES_NO_CHOICES)
    AUX = models.BooleanField(choices=YES_NO_CHOICES)
    FM_Expander = models.BooleanField(choices=YES_NO_CHOICES)

    windscreen_condition = models.CharField(choices=YES_NO_CHOICES)
    wipers_working = models.BooleanField(choices=YES_NO_CHOICES)
    seat_belts_functioning = models.BooleanField(choices=YES_NO_CHOICES)
    electric_mirrors_functioning = models.BooleanField(choices=YES_NO_CHOICES)
    electric_windows_functioning = models.BooleanField(choices=YES_NO_CHOICES)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    drivers_signature = JSignatureField()

    inspectors_first_name = models.CharField(max_length=50)
    inspectors_last_name = models.CharField(max_length=50)
    inspectors_signature = JSignatureField()
    additional_comments = models.TextField(blank=True) 
    dashboard_image = models.ImageField(upload_to='dashboard_images/', blank=True, null=True)
    damage_images = models.ManyToManyField(DamageImage, blank=True)
    
    
    

    def __str__(self):
        return f"Inspection for {self.car} on {self.date}"
