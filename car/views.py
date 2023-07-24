from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CarForm, CarModelForm
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

