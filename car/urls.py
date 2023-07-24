from django.urls import path
from . import views



app_name = 'car'
urlpatterns = [
   path('create_car/', views.create_car, name='create_car'),
   path('create_model/', views.create_model, name='create_model'),
]
