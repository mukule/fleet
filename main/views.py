from django.shortcuts import render,get_object_or_404
from car.models import Car

# Create your views here.
def dashboard(request):
    return render(request, 'main/dashboard.html')

def inventory(request):
    cars = Car.objects.all()
    return render(request, 'main/inventory.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'main/car_detail.html', {'car': car})