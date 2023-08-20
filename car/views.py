from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from.models import *
from dateutil.relativedelta import relativedelta



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


def insurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            insurance = form.save(commit=False)

            # Calculate end date based on duration
            duration = form.cleaned_data['duration']
            if duration == '1M':
                insurance.end_date = insurance.start_date + relativedelta(months=1)
            elif duration == '1Y':
                insurance.end_date = insurance.start_date + relativedelta(years=1)

            # Get the associated car's ID from the form
            car_id = form.cleaned_data['car'].id
            insurance.save()

            # Add a success message
            messages.success(request, 'Insurance added successfully.')

            # Redirect to the detailed view of the associated car
            return redirect('main:car_detail', car_id=car_id)

    else:
        form = InsuranceForm()

    return render(request, 'car/insurence.html', {'form': form})
