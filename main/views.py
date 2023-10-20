from django.shortcuts import render,get_object_or_404
from car.models import Car
from django.contrib.auth.decorators import login_required
from reservations.models import *
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
@login_required
def dashboard(request):
    # Retrieve the list of all cars from the database
    cars = Car.objects.all()

    # Pass the list of cars to the template context
    return render(request, 'main/dashboard.html', {'cars': cars})

def inventory(request):
    # Retrieve all Car objects
    cars = Car.objects.all()
    car_classes = CarClass.objects.all()

    # Apply filters based on user input
    car_class_filter = request.GET.get('car_class')
    number_plate_filter = request.GET.get('number_plate')

    if car_class_filter:
        cars = cars.filter(car_class=car_class_filter)

    if number_plate_filter:
        cars = cars.filter(number_plate__icontains=number_plate_filter)

    # Create a Paginator instance with filtered cars and specify the number of items per page
    paginator = Paginator(cars, 10)  # 10 cars per page

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page number
    page = paginator.get_page(page_number)

    return render(request, 'main/inventory.html', {'page': page, 'car_classes': car_classes})


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
    # Get the search query from the request's GET parameters
    search_query = request.GET.get('search')

    # Fetch all CarOut records
    car_outs = CarOut.objects.all()

    # Apply filter if a search query is provided
    if search_query:
        car_outs = car_outs.filter(
            Q(invoice_number__icontains=search_query) |  # Filter by invoice_number
            Q(full_name__icontains=search_query) |        # Filter by full_name
            Q(number_plate__icontains=search_query)      # Filter by number_plate
        )

    # Configure pagination (5 items per page)
    items_per_page = 10
    paginator = Paginator(car_outs, items_per_page)

    # Get the requested page number from the request's GET parameters
    page_number = request.GET.get('page')

    try:
        car_outs = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        car_outs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., page 9999), deliver the last page of results
        car_outs = paginator.page(paginator.num_pages)

    # Prepare the context dictionary
    context = {
        'car_outs': car_outs,
        'search_query': search_query  # Pass the search query to the template for displaying
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

def reports(request):
    # Total number of car classes
    total_car_classes = CarClass.objects.count()

    # Total number of cars
    total_cars = Car.objects.count()

    # Total number of cars without insurance
    cars_without_insurance = Car.objects.exclude(insurance__isnull=False).count()
     # Total number of cars with insurance coverage
    cars_with_coverage = Car.objects.filter(insurance__isnull=False).count()

    # Total number of cars with active insurance
    active_insurances = Insurance.objects.filter(
        car__isnull=False,
        start_date__lte=date.today(),
        end_date__gte=date.today(),
    ).count()

    # Total number of cars with insurance starting today or later
    future_start_insurances = Insurance.objects.filter(
        car__isnull=False,
        start_date__gt=date.today(),
    ).count()

    # Total number of cars with expired insurance
    expired_insurances = Insurance.objects.filter(
        Q(end_date__lt=date.today()) | Q(car__isnull=True)
    ).count()

    # Total amount of incomes
    total_income_amount = Income.objects.aggregate(total_amount=Sum('amount'))['total_amount']

   

    context = {
        'classes': total_car_classes,
        'cars': total_cars,
        'uncovered': cars_without_insurance,
        'covered': cars_with_coverage,
        'active': active_insurances,
        'expired': expired_insurances,
        'upcoming': future_start_insurances,
        'cashin': total_income_amount
    }

    return render(request, 'main/reports.html', context)


def income(request):
    # Retrieve all income records
    incomes = Income.objects.all()

    start_date_param = request.GET.get('start_date')
    end_date_param = request.GET.get('end_date')

    start_date = None
    end_date = None

    if start_date_param and end_date_param:
        try:
            # Convert start_date and end_date to datetime objects with time components
            start_date = datetime.strptime(start_date_param, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_param + ' 23:59:59', '%Y-%m-%d %H:%M:%S')

            # Convert the start and end dates to the timezone used in the Sale model
            start_date = timezone.make_aware(start_date, timezone.get_current_timezone())
            end_date = timezone.make_aware(end_date, timezone.get_current_timezone())

            # Filter sales within the specified date range
            incomes = incomes.filter(transaction_month__range=(start_date, end_date))
        except ValueError:
            # Handle invalid date format
            messages.warning(request, 'Invalid date format. Please use YYYY-MM-DD format.')

    # Calculate the total amounts
    total_gross_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    total_vat = incomes.aggregate(Sum('vat'))['vat__sum'] or 0
    total_net_amount = incomes.aggregate(Sum('net_amount'))['net_amount__sum'] or 0

    context = {
        'incomes': incomes,
        'total_gross_income': total_gross_income,
        'total_vat': total_vat,
        'total_net_amount': total_net_amount,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'main/income.html', context)
