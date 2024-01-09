from django.urls import path
from . import views


app_name = 'inspection'
urlpatterns = [
    path('', views.inspection, name='inspection'),
    path('success/', views.success, name='success'),
    path('inspections/', views.inspections, name='inspections'),
]
