from django.shortcuts import render,get_object_or_404
from car.models import Car
from django.contrib.auth.decorators import login_required
from reservations.models import *
from datetime import datetime
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
    car_out_count = car_out_instances.count()

    # Filter CarService instances by the number plate of the current car
    car_service_instances = CarService.objects.filter(car__number_plate=number_plate)
    last_service = CarService.objects.filter(car__number_plate=number_plate).order_by('-service_date').first()

    # Calculate the total cost for car service instances
    total_service_cost = car_service_instances.aggregate(total_cost=Sum('cost'))['total_cost']

    # Count the number of car service instances
    car_service_count = car_service_instances.count()

    # Filter Income instances by the number plate of the current car and sum the amounts
    total_income = Income.objects.filter(number_plate=number_plate).aggregate(total_amount=Sum('amount'))['total_amount']

    # Retrieve the insurance instance for the current car (if it exists)
    current_date = datetime.now().date()
    active_insurance = Insurance.objects.filter(car=car, start_date__lte=current_date, end_date__gte=current_date).first()
    print(active_insurance)

    # Calculate the number of days left before insurance expiry
    days_left = (active_insurance.end_date - current_date).days if active_insurance else None
    print(days_left)

    return render(request, 'main/car_detail.html', {
        'car': car,
        'car_out_instances': car_out_instances,
        'car_out_count': car_out_count,
        'car_service_instances': car_service_instances,
        'car_service_count': car_service_count,
        'total_cost': total_service_cost,
        'last_service': last_service,
        'total_income': total_income,
        'days_left': days_left
        
    })


def contracts(request):
    car_outs = CarOut.objects.all()
    for car_out in car_outs:
        print(car_out.pk)
    context = {
        'car_outs': car_outs
    }
    return render(request, 'main/contracts.html', context)

def contract(request, carout_id):
    carout = get_object_or_404(CarOut, pk=carout_id)
    
    try:
        # Retrieve the related CarInspection instance that matches the CarOut ID
        car_inspection = CarInspection.objects.get(car_out=carout)
        
        # Retrieve inspection items and their status associated with the CarInspection instance
        inspection_items = car_inspection.inspectionitemstatus_set.all()
    except CarInspection.DoesNotExist:
        inspection_items = []
    
    context = {
        'carout': carout,
        'inspection_items': inspection_items,
    }
    return render(request, 'main/contract.html', context)