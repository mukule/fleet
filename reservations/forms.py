from django import forms
from .models import *

class ReservationForm(forms.ModelForm):
    apply_normal_rates = forms.BooleanField(required=False, initial=False)
    add_VAT = forms.BooleanField(required=False, initial=False)
    daily_rates = forms.DecimalField(max_digits=8, decimal_places=2, required=False)
    standard_rate = forms.DecimalField(max_digits=8, decimal_places=2, required=False)

    class Meta:
        model = Reservation
        fields = ['car', 'client', 'start_date', 'end_date', 'apply_normal_rates', 'add_VAT', 'daily_rates', 'standard_rate']
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
            'office_telephone', 'residence_address', 'where_the_car_will_be_used_or_parked', 'payment_method', 'amount', 'vat', 'sub_total', 'deposit',
        ]
        labels = {
            'number_plate': 'Number Plate',
            'make': 'Make',
            'model': 'Model',
            'year': 'Year',
            'color': 'Color',
            'daily_rate': 'Daily Rate',
            'seating_capacity': 'Seating Capacity',
            'car_class': 'Car Class',
            'mileage': 'Mileage',
            'full_name': 'Full Name',
            'email': 'Email',
            'id_number': 'ID Number',
            'nationality': 'Nationality',
            'ld_appt_number': 'LD Appointment Number',
            'age': 'Age',
            'drivers_license_number': 'Driver\'s License Number',
            'country_of_issue': 'Country of Issue (Driver\'s License)',
            'license_expiry': 'License Expiry Date',
            'credit_card': 'Credit Card',
            'credit_card_number': 'Credit Card Number',
            'card_expiry': 'Card Expiry Date',
            'physical_address': 'Physical Address',
            'mobile_number': 'Mobile Number',
            'office_telephone': 'Office Telephone',
            'residence_address': 'Residence Address',
            'where_the_car_will_be_used_or_parked': 'Where the Car Will Be Used or Parked',
            'payment_method': 'Payment Method',
            'amount': 'Total Amount',
            'vat': 'VAT (16%)',
            'sub_total': 'Sub Total',
            'deposit': 'Deposit',
        }

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
        fields = ['fuel_out', 'kms_out', 'o_drivers_name', 'o_drivers_dl_no', 'o_country_of_issue', 'o_drivers_dl_expiry']
        labels = {
            'fuel_out': 'Fuel Tank Level',
            'kms_out': 'Kilometers Out',
            'o_drivers_name': 'Other Driver\'s Name',
            'o_drivers_dl_no': 'Other Driver\'s License Number',
            'o_country_of_issue': 'Other Drivers License Country of Issue',
            'o_drivers_dl_expiry': 'Other Driver\'s License Expiry Date',
        }
        widgets = {
            'fuel_out': forms.TextInput(attrs={'placeholder': 'Enter the level for fuel'}),
            'kms_out': forms.TextInput(attrs={'placeholder': 'Enter kilometers out'}),
            'o_drivers_name': forms.TextInput(attrs={'placeholder': 'Enter driver\'s name'}),
            'o_drivers_dl_no': forms.TextInput(attrs={'placeholder': 'Enter driver\'s license number'}),
            'o_country_of_issue': forms.TextInput(attrs={'placeholder': 'Enter country of issue'}),
            'o_drivers_dl_expiry': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control datepicker', 'type': 'date'}),
            # You can use 'class': 'form-control datepicker' or any other class you need for styling.
        }

class CarCheckInForm(forms.ModelForm):
    class Meta:
        model = CarOut
        fields = ['fuel_in', 'kms_in', 'damages_noted', 'balance']
        widgets = {
            'fuel_in': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter fuel in'}),
            'kms_in': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter kilometers in'}),
            'balance': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'damages_noted': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any noted damages/Car Performance'}),
        }