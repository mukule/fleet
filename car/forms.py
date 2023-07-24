from django import forms
from datetime import datetime
from .models import *

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class SelectYearWidget(forms.Select):
    def __init__(self, attrs=None, choices=()):
        years = self.get_years()
        super().__init__(attrs, choices=years)

    def get_years(self):
        now = datetime.now()
        current_year = now.year
        return [(year, year) for year in range(1900, current_year + 1)]

class CarForm(forms.ModelForm):
    year = forms.IntegerField(widget=SelectYearWidget(), label='Year', min_value=1900, max_value=datetime.now().year)

    class Meta:
        model = Car
        fields = ['name', 'number_plate', 'model', 'year', 'color', 'daily_rate', 'seating_capacity', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

        # Customize the "model" field's choices to display car model names in the form.
        car_models = CarModel.objects.all()
        self.fields['model'].queryset = car_models
        self.fields['model'].to_field_name = 'name'