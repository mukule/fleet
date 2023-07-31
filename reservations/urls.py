from django.urls import path
from . import views



app_name = 'reservations'
urlpatterns = [
   path('', views.reservations, name='reservations'),
   path('create_reservation/<int:car_id>/', views.create_reservation, name='create_reservation'),
   path('confirm_contract/<int:reservation_id>/', views.confirm_make_contract, name='confirm_make_contract'),
   path('make_contract/<int:reservation_id>/', views.make_contract, name='make_contract'),
   
]
