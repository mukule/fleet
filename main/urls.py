from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("inventory/", views.inventory, name="inventory"),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path("contracts/", views.contracts, name="contracts"),
    path('contract/<int:carout_id>/', views.contract, name='contract'),
    path("reports/", views.reports, name="reports"),
    path('incomes/', views.income, name='income'),
 
]