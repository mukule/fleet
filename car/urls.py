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
   
   
]
