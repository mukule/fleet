from django.urls import path
from . import views


app_name = 'inspection'
urlpatterns = [
    path('', views.inspection, name='inspection'),
    path('success/', views.success, name='success'),
    path('inspections/', views.inspections, name='inspections'),
    path('inspections/<int:pk>/', views.inspection_detail, name='inspection-detail'),
    path('del_inspections/<int:pk>/', views.delete_inspection, name='del-inspection'),
]
