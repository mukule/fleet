from django.urls import path
from .import views

from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('', views.custom_login, name='index'),
    path('logout', views.custom_logout, name='logout'),
    path('clients/', views.clients, name='clients'),
    path('add_client/', views.add_client, name='add_client'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
   
]