from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Inspection)
admin.site.register(EmergencyEquipment)
admin.site.register(YesNoChoice)
admin.site.register(FluidStatusChoice)
