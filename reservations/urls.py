from django.urls import path
from . import views



app_name = 'reservations'
urlpatterns = [
   path('', views.reservations, name='reservations'),
   path('create_reservation/<int:car_id>/', views.create_reservation, name='create_reservation'),
   path('update_reservation/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
   path('delete_invoice/<int:reservation_id>/', views.delete_invoice, name='delete_invoice'),
   path('confirm_contract/<int:reservation_id>/', views.confirm_make_contract, name='confirm_make_contract'),
   path('make_contract/<int:reservation_id>/', views.make_contract, name='make_contract'),
   path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
   path('car_inspection/<int:car_out_id>/<int:reservation_id>/', views.car_inspection, name='car_inspection'),
   path('update_carout/<int:carout_id>/<int:reservation_id>/', views.update_carout, name='update_carout'),
   path('checkin/', views.checkin, name='checkin'),
   path('carout/<int:carout_id>/', views.carout_detail, name='carout_detail'),
   path('carin_inspection/<int:carout_id>/', views.carin_inspection, name='carin_inspection'),
   path('edit-contract/<int:car_out_id>/', views.edit_contract, name='edit_contract'),
   path('update_car_inspection/<int:car_out_id>/', views.update_car_inspection, name='update_car_inspection'),
   path('edit_update_carout/<int:carout_id>/', views.edit_update_carout, name='edit_update_carout'),
   path('delete_carout/<int:carout_id>/', views.delete_carout, name='delete_carout'),

   
]
