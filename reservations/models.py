from django.db import models
from django.contrib.auth import get_user_model
from car.models import *
from users.models import *
from datetime import date
from django.utils import timezone


User = get_user_model()



class Reservation(models.Model):
    reservation_number = models.CharField(max_length=20, unique=True,null=True)  # Unique reservation number field
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    days = models.PositiveIntegerField(default=0, null=True)
    rates_applied = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True)

    def __str__(self):
        return f"Reservation #{self.reservation_number} for {self.car} by {self.client} (Staff: {self.staff})"