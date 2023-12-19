from django.urls import path
from . import views



app_name = 'car'
urlpatterns = [
   path('create_car/', views.create_car, name='create_car'),
   path('create_model/', views.create_model, name='create_model'),
   path('create_make/', views.create_make, name='create_make'),
   path('services/', views.service, name='service'),
   path('car_services/', views.car_services, name='car_services'),
   path('insurance/', views.insurance, name='insurance'),
   path('car-services/<int:car_service_id>/', views.car_service_detail, name='car_service'),
   path('car_service/edit/<int:service_id>/', views.edit_car_service, name='edit_car_service'),
   path('delete_car_service/<int:service_id>/', views.delete_car_service, name='delete_car_service'),
   path('insurances/', views.insurances, name='insurances'),
   path('edit/<int:car_id>/', views.edit_car, name='edit_car'),
   path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
   path('car-classes/', views.car_class, name='car_class'),
   path('add-vehicle-class/', views.add_vehicle_class, name='add_vehicle_class'),
   path('edit-vehicle-class/<int:pk>/', views.edit_vehicle_class, name='edit_vehicle_class'),
   path('delete-vehicle-class/<int:pk>/', views.delete_vehicle_class, name='delete_vehicle_class'),
    path('car_outs/s', views.rented_cars, name='rented_cars'),
    
]
