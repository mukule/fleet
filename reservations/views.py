from django.shortcuts import render,redirect,get_object_or_404
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

                    messages.success(request, 'Reservation created successfully.')
                    return redirect('reservations:reservations')  # Replace 'reservations' with the URL name for the reservations list page

        # If the form is not valid or there are errors, render the form again
        else:
            messages.error(request, 'Error creating reservation. Please check the form data.')

    else:
        form = ReservationForm(initial={'car': car})  # Pass the initial data for the 'car' field

    return render(request, 'reservations/reservation_form.html', {'form': form, 'car': car})