from django import forms
from .models import Reservation

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