from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from car.models import * 
from datetime import timedelta
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from django.utils.timezone import now, make_aware
import json 
from django.utils.crypto import get_random_string
from datetime import datetime, time
from decimal import Decimal


def reservations(request):
    # Retrieve all Car objects from the database
    cars_list = Car.objects.all()

    # Get the total number of cars in the fleet
    total_cars = cars_list.count()

    # Retrieve all car classes for the car class filter dropdown
    car_classes = CarClass.objects.all()

    # Check if the user submitted the filter form for number plate
    number_plate_filter = request.GET.get('number_plate', None)
    if number_plate_filter:
        cars_list = cars_list.filter(number_plate__icontains=number_plate_filter)

    # Check if the user submitted the filter form for car class
    car_class_filter = request.GET.get('car_class', None)
    if car_class_filter:
        cars_list = cars_list.filter(car_class_id=car_class_filter)

    # Retrieve reservations with a start date greater than the current date
    current_date = timezone.now().date()
    future_reservations = Reservation.objects.filter(start_date__gt=current_date)

    # Count the number of future reservations
    future_reservations_count = future_reservations.count()

    # Retrieve reservations that are active on the current date
    current_reservations = Reservation.objects.filter(start_date__lte=current_date, end_date__gte=current_date)

    # Count the number of current reservations
    current_reservations_count = current_reservations.count()

    # Retrieve reservations made on the current date
    reservations_made_today = Reservation.objects.filter(created_at__gte=current_date, created_at__lt=current_date + timezone.timedelta(days=1))

    # Count the number of reservations made today
    reservations_made_today_count = reservations_made_today.count()

    # Get the list of car IDs from current reservations and reservations made today
    reserved_car_ids = current_reservations.values_list('car_id', flat=True)
    reserved_today_car_ids = reservations_made_today.values_list('car_id', flat=True)

    # Get the list of available car IDs (cars not on rent)
    available_car_ids = cars_list.exclude(id__in=reserved_car_ids).exclude(id__in=reserved_today_car_ids)

    # Filter the cars_list to get only the available cars
    available_cars_list = cars_list.filter(id__in=available_car_ids)

    # Calculate the available cars in the fleet (total fleet minus the cars that are currently on rent)
    available_cars_count = available_cars_list.count()

    # Get the total number of car classes
    total_car_classes = car_classes.count()

    # Create lists to store car class names and corresponding car counts and available car counts
    car_class_names = []
    car_counts = []
    available_cars_class_counts = []

    for car_class in car_classes:
        car_class_names.append(car_class.name)
        car_count = Car.objects.filter(car_class=car_class).count()
        car_counts.append(car_count)
        available_cars_class_count = Car.objects.filter(car_class=car_class, id__in=available_car_ids).count()
        available_cars_class_counts.append(available_cars_class_count)
        print(f"Car Class: {car_class.name}, Total Cars: {car_count}, Available Cars: {available_cars_class_count}")

    return render(
        request,
        'reservations/reservations.html',
        {
            'cars_list': cars_list,
            'total_cars': total_cars,
            'available_cars_list': available_cars_list,
            'available_cars_count': available_cars_count,
            'car_classes': car_classes,
            'future_reservations': future_reservations,
            'future_reservations_count': future_reservations_count,
            'current_reservations': current_reservations,
            'current_reservations_count': current_reservations_count,
            'reservations_made_today': reservations_made_today,
            'reservations_made_today_count': reservations_made_today_count,
           'car_class_names': json.dumps(car_class_names),
           'car_counts': json.dumps(car_counts),
           'available_cars_class_counts': json.dumps(available_cars_class_counts),
        }
    )

def generate_unique_reservation_number():
    # Generate a 4-digit random string
    return get_random_string(length=4, allowed_chars='0123456789')

@login_required  # This decorator ensures the user is logged in to access the view
def create_reservation(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Check if the start date is less than the current date
            if start_date < timezone.now():
                messages.error(request, "Start date cannot be in the past.")
            # Check if the end date is less than the start date
            elif end_date < start_date:
                messages.error(request, "End date cannot be before the start date.")
            else:
                # Check if the car is already reserved for any overlapping period
                overlapping_reservations = Reservation.objects.filter(
                    car=car,
                    start_date__lte=end_date,
                    end_date__gte=start_date,
                )

                if overlapping_reservations.exists():
                    reserved_dates = [
                        f"{reservation.start_date.strftime('%Y-%m-%d')} to {reservation.end_date.strftime('%Y-%m-%d')}"
                        for reservation in overlapping_reservations
                    ]
                    reserved_dates_str = ', '.join(reserved_dates)
                    messages.error(request, f"Car is already reserved for the following dates: {reserved_dates_str}.")
                else:
                    reservation = form.save(commit=False)

                    # Generate a unique 4-digit reservation number
                    unique_number = generate_unique_reservation_number()
                    while Reservation.objects.filter(reservation_number=unique_number).exists():
                        unique_number = generate_unique_reservation_number()

                    # Save the unique reservation number
                    reservation.reservation_number = unique_number

                    # Calculate the duration in days
                    duration_days = (end_date - start_date).days + 1

                    if form.cleaned_data['apply_normal_rates']:
                        # Using normal rates
                        if duration_days < 7:
                            rate_before_discount = car.daily_rate
                        elif duration_days >= 7 and duration_days < 30:
                            rate_before_discount = car.weekly_rate
                        else:
                            rate_before_discount = car.monthly_rate

                        # Save the rates before applying the discount in the daily_rates field
                        reservation.daily_rates = rate_before_discount
                    else:
                        # Using custom rates
                        rate_before_discount = form.cleaned_data['daily_rates']

                        # Check if daily rates are provided when normal rates are not used
                        if not rate_before_discount:
                            messages.error(request, "Please enter the daily rates.")
                            return render(request, 'reservations/reservation_form.html', {'form': form, 'car': car})

                    # Convert the rate_before_discount to Decimal before performing calculations
                    rate_before_discount = Decimal(str(rate_before_discount))

                    # Calculate the total amount before VAT
                    reservation.rate = rate_before_discount * duration_days

                    # Apply VAT if selected
                    if form.cleaned_data['add_VAT']:
                        vat_rate = 0.16  # You can adjust this rate accordingly
                        reservation.vat = reservation.rate * Decimal(str(vat_rate))

                    # Calculate the total amount (excluding VAT) and assign to total_amount field
                    reservation.total_amount = reservation.rate

                    # Calculate the total amount including VAT (if applicable) and assign to total_amount_vat field
                    reservation.total_amount_vat = reservation.rate + reservation.vat

                    # Assign the car, client, and staff, then save the reservation
                    reservation.car = car
                    reservation.staff = request.user  # Set the staff field to the logged-in user
                    reservation.client = form.cleaned_data['client']
                    reservation.days = duration_days  # Save the duration in days
                    reservation.save()

                    # messages.success(request, 'Reservation created successfully.')
                    return redirect('reservations:confirm_make_contract', reservation_id=reservation.id)  # Replace 'reservations' with the URL name for the reservations list page

        # If the form is not valid or there are errors, render the form again
        else:
            messages.error(request, 'Error creating reservation. Please check the form data.')

    else:
        form = ReservationForm(initial={'car': car})  # Pass the initial data for the 'car' field

    return render(request, 'reservations/reservation_form.html', {'form': form, 'car': car})

def confirm_make_contract(request, reservation_id):
    # Retrieve the reservation object using the reservation_id
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Any additional code to process the reservation data or prepare data for the contract template

    # Pass the reservation object to the template context
    return render(request, 'reservations/confirm_contract.html', {'reservation': reservation})

def make_contract(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    car = reservation.car
    client = reservation.client

    initial_data = {
        # car details
        'number_plate': car.number_plate,
        'make': car.make.name if car.make else None,
        'model': car.model.name if car.model else None,
        'year': car.year,
        'color': car.color,
        'daily_rate': car.daily_rate,
        'weekly_rate': car.weekly_rate,
        'monthly_rate': car.monthly_rate,
        'seating_capacity': car.seating_capacity,
        'car_class': car.car_class.name if car.car_class else None,
        'mileage': car.mileage,
        'amount': reservation.total_amount_vat,

        # renter details
        'full_name': f"{client.first_name} {client.last_name}",
        'email': client.email,
        'id_number': client.id_number,
        'nationality': client.nationality,
        'age': client.age,
        'drivers_license_number': client.drivers_license_number,
        'country_of_issue': client.country_of_issue,
        'license_expiry': client.license_expiry,
        'credit_card': client.credit_card,
        'credit_card_number': client.credit_card_number,
        'card_expiry': client.card_expiry,
        'physical_address': client.physical_address,
        'mobile_number': client.phone_number,
        'office_telephone': client.office_telephone,
        'residence_address': client.residence_address,
    }

    if request.method == 'POST':
        combined_form = CarOutForm(request.POST, initial=initial_data)
        if combined_form.is_valid():
            car_out_instance = combined_form.save(commit=False)
            # Update the renter-related fields in the CarOut instance from the Client model
            car_out_instance.full_name = f"{client.first_name} {client.last_name}"
            car_out_instance.email = client.email
            car_out_instance.id_number = client.id_number
            car_out_instance.nationality = client.nationality
            car_out_instance.age = client.age
            car_out_instance.drivers_license_number = client.drivers_license_number
            car_out_instance.country_of_issue = client.country_of_issue
            car_out_instance.license_expiry = client.license_expiry
            car_out_instance.credit_card = client.credit_card
            car_out_instance.credit_card_number = client.credit_card_number
            car_out_instance.card_expiry = client.card_expiry
            car_out_instance.physical_address = client.physical_address
            car_out_instance.mobile_number = client.phone_number
            car_out_instance.office_telephone = client.office_telephone
            car_out_instance.residence_address = client.residence_address
            car_out_instance.residence_address = client.residence_address
            car_out_instance.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('reservations:car_inspection', car_out_id=car_out_instance.id)
    else:
        combined_form = CarOutForm(initial=initial_data)

    return render(request, 'reservations/contract_details.html', {'combined_form': combined_form, 'reservation': reservation})

def car_inspection(request, car_out_id):
    car_out_instance = get_object_or_404(CarOut, id=car_out_id)
    inspection_items = InspectionItem.objects.all()
    inspection_item_statuses = InspectionItemStatus.objects.filter(car_inspection__car_out=car_out_instance)

    if request.method == 'POST':
        form = CarInspectionForm(inspection_items, request.POST)
        if form.is_valid():
            # Get or create the CarInspection instance associated with the car_out_instance
            car_inspection_instance, created = CarInspection.objects.get_or_create(car_out=car_out_instance)
            
            # Loop through inspection items and update their statuses
            for item in inspection_items:
                checked_out = form.cleaned_data[f"checked_out_{item.id}"]
                inspection_item_status, _ = InspectionItemStatus.objects.get_or_create(
                    car_inspection=car_inspection_instance,
                    inspection_item=item
                )
                inspection_item_status.checked_out = checked_out
                inspection_item_status.save()
            
            # Update the fuel_out and kms_out values
            fuel_out = form.cleaned_data['fuel_out']
            kms_out = form.cleaned_data['kms_out']
            car_inspection_instance.fuel_out = fuel_out
            car_inspection_instance.kms_out = kms_out
            car_inspection_instance.save()

            # Redirect to a success page or perform other actions
            return redirect('reservations:inspection_success')
    else:
        initial_data = {}
        for item_status in inspection_item_statuses:
            initial_data[f"checked_out_{item_status.inspection_item.id}"] = item_status.checked_out
        form = CarInspectionForm(inspection_items, initial=initial_data)

    return render(request, 'reservations/car_inspection.html', {
        'car_out_instance': car_out_instance,
        'inspection_items': inspection_items,
        'inspection_item_statuses': inspection_item_statuses,
        'form': form,
    })
