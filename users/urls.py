from django.urls import path
from .import views

from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('index', views.custom_login, name='index'),
    path('logout', views.custom_logout, name='logout'),
   
]