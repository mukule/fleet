from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
   
    
]