from django.contrib import admin
from .models import *

@admin.register(CarClass)
class CarClassAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'make']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['number_plate', 'make', 'model', 'year', 'color', 'daily_rate', 'seating_capacity', 'car_class']
    list_filter = ['make', 'model', 'year', 'color', 'car_class']
    search_fields = ['number_plate', 'make__name', 'model__name', 'color']

    # If you want to customize the fields in the edit form, you can use the fields attribute.
    # For example, to show the image field separately from other fields, use:
    # fields = ['number_plate', 'make', 'model', 'year', 'color', 'daily_rate', 'seating_capacity', 'car_class']
    # readonly_fields = ['image']  # If you want to make the image field read-only.

    # If you prefer to use fieldsets to group fields in the edit form, you can do it like this:
    # fieldsets = (
    #     (None, {
    #         'fields': ('number_plate', 'make', 'model', 'year', 'color', 'daily_rate', 'seating_capacity', 'car_class')
    #     }),
    #     ('Car Image', {
    #         'fields': ('image',),
    #         'classes': ('collapse',)  # To make the image field initially collapsed.
    #     }),
    # )

# If you have any other models to register, add them here following the same pattern as above.

admin.site.register(ServiceCompany)
admin.site.register(CarService)
admin.site.register(Insurance)

