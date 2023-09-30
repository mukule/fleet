from django.db import models
from django.contrib.auth import get_user_model
from car.models import *
from users.models import *
from datetime import date
from django.utils import timezone
from django.core.validators import MaxValueValidator



User = get_user_model()



class Taxes(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.rate}%"
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    reservation_number = models.CharField(max_length=20, unique=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()  # Change to DateTimeField
    end_date = models.DateTimeField()    # Change to DateTimeField
    created_at = models.DateTimeField(default=timezone.now)
    days = models.PositiveIntegerField(default=0, null=True)
    daily_rates = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True)
    apply_normal_rates = models.BooleanField(default=False)  # Checkbox for using custom rates
    add_VAT = models.BooleanField(default=False)          # Checkbox for adding tax
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # Set to null=True
    vat = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # Default VAT is set to 0
    total_amount_vat = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return f"Reservation #{self.reservation_number} for {self.car} by {self.client} (Staff: {self.staff})"
    
class Fuel(models.Model):
    LEVEL_CHOICES = (
        ('1/4', '1/4'),
        ('1/2', '1/2'),
        ('3/4', '3/4'),
        ('Full', 'Full'),
    )
    
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES)
    
    def __str__(self):
        return self.level
    
class CarOut(models.Model):
    # Car details
    invoice_number = models.CharField(max_length=20, null=True)
    number_plate = models.CharField(max_length=20)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    seating_capacity = models.PositiveIntegerField()
    car_class = models.CharField(max_length=100)
    mileage = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(999999)])
    start_date = models.DateTimeField(null=True, blank=True)  # Change to DateTimeField
    end_date = models.DateTimeField(null=True, blank=True)    #
    created_at = models.DateTimeField(default=timezone.now)
    approver = models.CharField(max_length=150, null=True, blank=True)

    # Renter details
    full_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    ld_appt_number = models.CharField(max_length=50, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    drivers_license_number = models.CharField(max_length=50, null=True, blank=True)
    country_of_issue = models.CharField(max_length=50, null=True, blank=True)
    license_expiry = models.DateField(null=True, blank=True)
    credit_card = models.CharField(max_length=50, null=True, blank=True)
    credit_card_number = models.CharField(max_length=16, null=True, blank=True)
    card_expiry = models.DateField(null=True, blank=True)
    physical_address = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    office_telephone = models.CharField(max_length=20, null=True, blank=True)
    residence_address = models.CharField(max_length=100, null=True, blank=True)  # Updated field name
    where_the_car_will_be_used_or_parked = models.CharField(max_length=100, null=True, blank=True)  # Updated field name
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Fuel and Kilometers
    o_drivers_name = models.CharField(max_length=150, null=True, blank=True)
    o_drivers_dl_no = models.CharField(max_length=50, null=True, blank=True)
    o_country_of_issue = models.CharField(max_length=50, null=True, blank=True)
    o_drivers_dl_expiry = models.DateField(null=True, blank=True)
    # Fuel and Kilometers
    fuel_out = models.CharField(max_length=50, blank=True, null=True)
    fuel_in = models.CharField(max_length=50, blank=True, null=True)
    kms_out = models.PositiveIntegerField(null=True, blank=True)
    kms_in = models.PositiveIntegerField(null=True, blank=True)
    kms_driven = models.PositiveIntegerField(null=True, blank=True)
    kms_allowed = models.PositiveIntegerField(null=True, blank=True)
    damages_noted = models.TextField(null=True, blank=True)
    checked_in = models.BooleanField(default=False)
    check_in_date_time = models.DateTimeField(null=True, blank=True)  # Change to DateTimeField

    def __str__(self):
        return f"{self.make} {self.model} - {self.number_plate}"
    
class Income(models.Model):
    number_plate = models.CharField(max_length=20, null=True, blank=True)
    invoice_number = models.CharField(max_length=20)
    client = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Income: {self.invoice_number}"
    


     
class CarInspection(models.Model):
    car_out = models.ForeignKey(CarOut, on_delete=models.CASCADE)
    inspection_date = models.DateTimeField(auto_now_add=True)
    inspection_items = models.ManyToManyField('InspectionItem', through='InspectionItemStatus')
    
    

class InspectionItem(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class InspectionItemStatus(models.Model):
    car_inspection = models.ForeignKey(CarInspection, on_delete=models.CASCADE)
    inspection_item = models.ForeignKey(InspectionItem, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.car_inspection} - {self.inspection_item}"
