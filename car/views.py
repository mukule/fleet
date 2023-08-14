from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from.models import *


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully.')
            return redirect('main:inventory')  # Redirect to the car list page after successful form submission
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = CarForm()

    return render(request, 'car/create_car.html', {'form': form})

def create_make(request):
    if request.method == 'POST':
        form = CarMakeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car make created successfully!')
            return redirect('car:create_model')  # Redirect to the car make list view after successful creation
        else:
            messages.error(request, 'There was an error creating the car make. Please check the form and try again.')
    else:
        form = CarMakeForm()

    return render(request, 'car/create_make.html', {'form': form})

def create_model(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car model added successfully.')
            return redirect('car:create_car')  # Redirect to the create car page after successful form submission
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = CarModelForm()

    return render(request, 'car/create_model.html', {'form': form})



def service(request):
    if request.method == 'POST':
        form = CarServiceForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform other actions
            return redirect('reservations:reservations')
    else:
        form = CarServiceForm()
    
    return render(request, 'car/service.html', {'form': form})

def car_services(request):
    car_services = CarService.objects.all().order_by('-service_date')
    return render(request, 'car/car_service.html', {'car_services': car_services})