from django.urls import path
from . import views



app_name = 'invoices'
urlpatterns = [
   path('', views.invoices, name='invoices'),
   path('invoices/<int:reservation_id>/', views.invoice_detail, name='invoice_detail'),
   path('generate_invoice/<int:reservation_id>/', views.generate_invoice, name='generate_invoice'),
   
  
   
]
