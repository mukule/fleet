from django import forms
from .models import *

class ReservationForm(forms.ModelForm):
    apply_normal_rates = forms.BooleanField(required=False, initial=False)
    add_VAT = forms.BooleanField(required=False, initial=False)
    daily_rates = forms.DecimalField(max_digits=8, decimal_places=2, required=False)

    class Meta:
        model = Reservation
        fields = ['car', 'client', 'start_date', 'end_date', 'apply_normal_rates', 'add_VAT', 'daily_rates']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD HH:MM'
        self.fields['end_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD HH:MM'


class CarOutForm(forms.ModelForm):
    class Meta:
        model = CarOut
        fields = [
            'number_plate', 'make', 'model', 'year', 'color', 'daily_rate', 'seating_capacity',
            'car_class', 'mileage', 'full_name', 'email', 'id_number', 'nationality', 'ld_appt_number', 'age',
            'drivers_license_number', 'country_of_issue', 'license_expiry', 'credit_card',
            'credit_card_number', 'card_expiry', 'physical_address', 'mobile_number',
            'office_telephone', 'residence_address', 'where_the_car_will_be_used_or_parked','payment_method', 'amount', 'deposit',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set form control class to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        initial_data = kwargs.get('initial', {})
        if initial_data.get('make'):
            initial_data['make'] = CarMake.objects.get(name=initial_data['make'])
        if initial_data.get('model'):
            initial_data['model'] = CarModel.objects.get(name=initial_data['model'])
        
        # Set initial data
        self.initial = initial_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Additional processing specific to CarOut
        # For example, you can set fields like 'full_name', 'nationality', etc. here

        if commit:
            instance.save()
        return instance

class CarInspectionForm(forms.Form):
    def __init__(self, inspection_items, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in inspection_items:
            self.fields[f'checked_out_{item.id}'] = forms.BooleanField(
                required=False,
                label=item.name  # Use the item name as the label
            )

class CarInInspectionForm(CarInspectionForm):
    def __init__(self, inspection_items, *args, **kwargs):
        super().__init__(inspection_items, *args, **kwargs)
        for item in inspection_items:
            self.fields[f'checked_out_{item.id}'] = forms.BooleanField(
                required=False,
                label=f' {item.name}'  # Customize the label for check out
            )

            
class CarOutUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = CarOut
        fields = ['fuel_out', 'kms_out']



class CarCheckInForm(forms.ModelForm):
    class Meta:
        model = CarOut
        fields = ['fuel_in', 'kms_in', 'damages_noted']


