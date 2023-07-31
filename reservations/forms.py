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
        fields = ['number_plate', 'make', 'model', 'year', 'color', 'daily_rate', 'seating_capacity', 'car_class', 'mileage']

    def __init__(self, *args, **kwargs):
        initial_data = kwargs.get('initial', {})
        if initial_data.get('make'):
            # Convert make name to the corresponding CarMake object
            initial_data['make'] = CarMake.objects.get(name=initial_data['make'])
        if initial_data.get('model'):
            # Convert model name to the corresponding CarModel object
            initial_data['model'] = CarModel.objects.get(name=initial_data['model'])

        super().__init__(*args, **kwargs)

        # Set initial data
        self.initial = initial_data