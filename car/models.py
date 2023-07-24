from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20, unique=True)  # Enforce uniqueness for number_plate
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    seating_capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.model.name} - {self.year}, {self.color}, Seats: {self.seating_capacity}) - {self.number_plate}"
