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

    def __str__(self):
        return f"Reservation #{self.reservation_number} for {self.car} by {self.client} (Staff: {self.staff})"

class CarOut(models.Model):
    # Car details
    number_plate = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=100)  # Assuming CarMake is a CharField or related model not used
    model = models.CharField(max_length=100)  # Assuming CarModel is a CharField or related model not used
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    seating_capacity = models.PositiveIntegerField()
    car_class = models.CharField(max_length=100)  # Assuming CarClass is a CharField or related model not used
    mileage = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(999999)])  # 6-digit mileage

    def __str__(self):
        return f"{self.make} {self.model} - {self.number_plate}"