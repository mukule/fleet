from django.shortcuts import render,get_object_or_404
from car.models import Car
from django.contrib.auth.decorators import login_required
from reservations.models import *
from django.db.models import Sum


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

    # Filter CarService instances by the number plate of the current car
    car_service_instances = CarService.objects.filter(car__number_plate=number_plate)

    # Retrieve the last car service instance for the current car
    last_service = CarService.objects.filter(car__number_plate=number_plate).order_by('-service_date').first()

    # Calculate the total cost for car service instances
    total_service_cost = car_service_instances.aggregate(total_cost=Sum('cost'))['total_cost']

    # Count the number of car service instances
    car_service_count = car_service_instances.count()

    return render(request, 'main/car_detail.html', {
        'car': car,
        'car_out_instances': car_out_instances,
        'car_service_instances': car_service_instances,
        'car_service_count': car_service_count,
        'total_cost': total_service_cost,
        'last_service': last_service
    })