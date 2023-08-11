from django.contrib import admin
from .models import *

admin.site.register(Reservation)

admin.site.register(Taxes)
admin.site.register(CarOut)
admin.site.register(PaymentMethod)
admin.site.register(InspectionItem)
admin.site.register(InspectionItemStatus)
admin.site.register(CarInspection)
