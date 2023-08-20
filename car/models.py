from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

class CarClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    number_plate = models.CharField(max_length=20, unique=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    weekly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    monthly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    seating_capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    car_class = models.ForeignKey(CarClass, on_delete=models.SET_NULL, null=True)
    mileage = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(999999)], null=True)  # 6-digit mileage

    def __str__(self):
        make_name = self.make.name if self.make else "N/A"
        model_name = self.model.name if self.model else "N/A"
        return f"{make_name} {model_name} - {self.number_plate}"
    

class ServiceCompany(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CarService(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Update the default value
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car} - Service on {self.service_date} by {self.service_company}"
    
class Insurance(models.Model):
    DURATION_CHOICES = [
        ('1M', '1 Month'),
        ('1Y', '1 Year'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    insurance_company = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    renew = models.BooleanField(default=False)
    duration = models.CharField(max_length=2, choices=DURATION_CHOICES, null=True)  # New duration field

    def __str__(self):
        return f"{self.car} - Insurance {self.policy_number}"
