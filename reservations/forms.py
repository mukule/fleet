from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    discount = forms.DecimalField(max_digits=8, decimal_places=2, initial=0, min_value=0, max_value=100)

    class Meta:
        model = Reservation
        fields = ['car', 'client', 'start_date', 'end_date', 'discount']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['end_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
