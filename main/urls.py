from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("inventory", views.inventory, name="inventory"),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
   
    
]