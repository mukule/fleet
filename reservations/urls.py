from django.urls import path
from . import views



app_name = 'reservations'
urlpatterns = [
   path('reservations/', views.reservations, name='reservations'),
   path('create_reservation/<int:car_id>/', views.create_reservation, name='create_reservation'),
  
   
]
