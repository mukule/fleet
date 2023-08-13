from django.shortcuts import render,get_object_or_404
from car.models import Car
from django.contrib.auth.decorators import login_required
from reservations.models import *


# Create your views here.
@login_required
def dashboard(request):
    # Retrieve the list of all cars from the database
    cars = Car.objects.all()

    # Pass the list of cars to the template context
    return render(request, 'main/dashboard.html', {'cars': cars})

def inventory(request):
    cars = Car.objects.all()
    return render(request, 'main/inventory.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    number_plate = car.number_plate

    # Filter CarOut instances by the number plate of the current car
    car_out_instances = CarOut.objects.filter(number_plate=number_plate)

    return render(request, 'main/car_detail.html', {'car': car, 'car_out_instances': car_out_instances})