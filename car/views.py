from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from.models import *
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.db.models import Q
from reservations.models import *

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            # Validate the number plate format
            number_plate = form.cleaned_data.get('number_plate')
            if not is_valid_number_plate(number_plate):
                messages.error(request, 'Number plate format should be like ABC 123X (3 letters, 3 digits, 1 letter).')
            else:
                # Set initial value for mileage to 0
                form.initial['mileage'] = 0
                form.save()
                messages.success(request, 'Car added successfully.')
                return redirect('main:inventory')  # Redirect to the car list page after successful form submission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Set initial value for mileage to 0 when creating the form
        form = CarForm(initial={'mileage': 0})

    return render(request, 'car/create_car.html', {'form': form})


def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            number_plate = form.cleaned_data.get('number_plate')
            if not is_valid_number_plate(number_plate):
                messages.error(request, 'Number plate format should be like ABC 123X (3 letters, 3 digits, 1 letter).')
            else:
                form.save()
                messages.success(request, 'Car updated successfully.')
                return redirect('main:inventory')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Initialize the form fields with initial data
        initial_data = {
            'model': car.model,
            'make': car.make,
            'car_class': car.car_class,
            # Add other fields as needed
        }
        form = CarForm(instance=car, initial=initial_data)

    return render(request, 'car/edit_car.html', {'form': form, 'car': car})


def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    car.delete()
    messages.success(request, 'Car deleted successfully.')
    return redirect('main:inventory')


# Define a function to check the number plate format
def is_valid_number_plate(number_plate):
    import re
    pattern = r'^[A-Z]{3}\s\d{3}[A-Z]$'  # Example format: ABC 123X (3 letters, 3 digits, 1 letter)
    return bool(re.match(pattern, number_plate))



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
            # Get the related car instance from the form
            car = form.cleaned_data.get('car')

            # Check if the car instance exists and has mileage
            if car and car.mileage is not None:
                # Set the 'current_kms' field to the car's mileage
                car_service = form.save(commit=False)
                car_service.current_kms = car.mileage
                car_service.save()

                # Add a success message
                messages.success(request, 'Car service record saved successfully.')

                # Redirect to a success page or perform other actions
                return redirect('reservations:reservations')
            else:
                # Add an error message if the car or mileage is missing
                messages.error(request, 'Error: Selected car or car mileage is missing.')
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Error: Form is not valid.')

    else:
        form = CarServiceForm()

    return render(request, 'car/service.html', {'form': form})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def car_services(request):
    # Get the filter parameters from the request
    search_query = request.GET.get('search')
    
    # Start with all CarService objects
    car_services = CarService.objects.all().order_by('-service_date')
    
    # Apply filters based on search_query
    if search_query:
        car_services = car_services.filter(
            Q(car__make__name__icontains=search_query) |  # Filter by car make name
            Q(car__model__name__icontains=search_query) |  # Filter by car model name
            Q(service_by__icontains=search_query)  # Filter by service provider
        )
    
    # Configure pagination
    page_number = request.GET.get('page', 1)
    items_per_page = 10  # Set the number of items per page
    paginator = Paginator(car_services, items_per_page)
    
    try:
        car_services = paginator.page(page_number)
    except PageNotAnInteger:
        car_services = paginator.page(1)
    except EmptyPage:
        car_services = paginator.page(paginator.num_pages)
    
    return render(request, 'car/car_service.html', {'car_services': car_services})

def car_service_detail(request, car_service_id):
    # Get the CarService record with the given ID or return a 404 error if not found
    car_service = get_object_or_404(CarService, pk=car_service_id)
    
    return render(request, 'car/car_service_detail.html', {'car_service': car_service})

def edit_car_service(request, service_id):
    car_service = get_object_or_404(CarService, pk=service_id)

    if request.method == 'POST':
        form = CarServiceForm(request.POST, instance=car_service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car service record updated successfully.')
            return redirect('car:car_services')
        else:
            messages.error(request, 'Error: Please correct the errors below.')
    else:
        form = CarServiceForm(instance=car_service)

    return render(request, 'car/edit_car_service.html', {'form': form, 'car_service': car_service})

def delete_car_service(request, service_id):
    car_service = get_object_or_404(CarService, pk=service_id)
    car_service.delete()
    messages.success(request, 'Car service record deleted successfully.')
    return redirect('car:car_services')  # Redirect to the list of Car Services

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

# Display view for an insurance instance
def insurances(request):
    insurances = Insurance.objects.all()
    return render(request, 'car/insurances.html', {'insurances': insurances})

# Edit view for an insurance instance
def edit_insurance(request, insurance_id):
    insurance = get_object_or_404(Insurance, pk=insurance_id)
    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            insurance = form.save(commit=False)

            # Calculate end date based on duration
            duration = form.cleaned_data['duration']
            if duration == '1M':
                insurance.end_date = insurance.start_date + relativedelta(months=1)
            elif duration == '1Y':
                insurance.end_date = insurance.start_date + relativedelta(years=1)

            insurance.save()

            # Add a success message
            messages.success(request, 'Insurance updated successfully.')

            # Redirect to the detailed view of the insurance instance
            return redirect('car:view_insurance', insurance_id=insurance.id)
    else:
        form = InsuranceForm(instance=insurance)

    return render(request, 'car/edit_insurance.html', {'form': form, 'insurance': insurance})

# Delete view for an insurance instance
def delete_insurance(request, insurance_id):
    insurance = get_object_or_404(Insurance, pk=insurance_id)
    car_id = insurance.car.id  # Get the associated car's ID before deletion
    insurance.delete()

    # Add a success message
    messages.success(request, 'Insurance deleted successfully.')

    # Redirect to the detailed view of the associated car
    return redirect('main:car_detail', car_id=car_id)


def car_class(request):
    car_classes = CarClass.objects.all()
    return render(request, 'car/car_class.html', {'vehicle_classes': car_classes})

def add_vehicle_class(request):
    if request.method == 'POST':
        form = CarClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car:car_class')  # Redirect to the list of vehicle classes after adding
    else:
        form = CarClassForm()

    return render(request, 'car/add_vehicle_class.html', {'form': form})

def edit_vehicle_class(request, pk):
    vehicle_class = get_object_or_404(CarClass, pk=pk)

    if request.method == 'POST':
        form = CarClassForm(request.POST, instance=vehicle_class)
        if form.is_valid():
            form.save()
            return redirect('car:car_class')  # Redirect to the list of vehicle classes after editing
    else:
        form = CarClassForm(instance=vehicle_class)

    return render(request, 'car/edit_vehicle_class.html', {'form': form, 'vehicle_class': vehicle_class})

def delete_vehicle_class(request, pk):
    vehicle_class = get_object_or_404(CarClass, pk=pk)
    vehicle_class.delete()
    return redirect('car:car_class')  


def rented_cars(request):
    carouts = CarOut.objects.all().order_by('-created_at')[:5]
    return render(request, 'car/carouts.html', {'carouts': carouts})

