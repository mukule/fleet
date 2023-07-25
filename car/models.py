from django.db import models

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
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    weekly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    monthly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    seating_capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    car_class = models.ForeignKey(CarClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.make.name} - {self.model.name} ({self.year}, {self.color}, Seats: {self.seating_capacity}) - {self.number_plate}"
