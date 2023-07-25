from django.shortcuts import render,redirect,get_object_or_404
from car.models import * 
from datetime import timedelta
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone



from datetime import date

def reservations(request):
    # Retrieve all Car objects from the database
    cars_list = Car.objects.all()

    # Get the total number of cars
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
    reservations_made_today = Reservation.objects.filter(created_at__date=current_date)
    print(reservations_made_today)
    print("Current Date:", current_date)


    # Count the number of reservations made today
    reservations_made_today_count = reservations_made_today.count()

    return render(
        request,
        'reservations/reservations.html',
        {
            'cars_list': cars_list,
            'total_cars': total_cars,
            'car_classes': car_classes,
            'future_reservations': future_reservations,
            'future_reservations_count': future_reservations_count,
            'current_reservations': current_reservations,
            'current_reservations_count': current_reservations_count,
            'reservations_made_today': reservations_made_today,
            'reservations_made_today_count': reservations_made_today_count,
        }
    )


@login_required  # This decorator ensures the user is logged in to access the view
def create_reservation(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)

            # Calculate the duration in days
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            duration_days = (end_date - start_date).days + 1

            # Set the rates based on the duration
            if duration_days < 7:
                reservation.rate = car.daily_rate * duration_days
            elif duration_days >= 7 and duration_days < 30:
                reservation.rate = car.weekly_rate * (duration_days // 7)
            else:
                reservation.rate = car.monthly_rate * (duration_days // 30)

            # Apply the discount
            reservation.rate -= reservation.rate * (reservation.discount / 100)

            # Assign the car and staff, then save the reservation
            reservation.car = car
            reservation.staff = request.user  # Set the staff field to the logged-in user
            reservation.save()

            messages.success(request, 'Reservation created successfully.')
            return redirect('reservations:reservations')  # Replace 'reservation_success' with the URL name for the success page
        else:
            messages.error(request, 'Error creating reservation. Please check the form data.')

    else:
        form = ReservationForm(initial={'car': car})  # Pass the initial data for the 'car' field

    return render(request, 'reservations/reservation_form.html', {'form': form, 'car': car})
