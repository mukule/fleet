from django import forms
from datetime import datetime
from .models import *

class CarModelForm(forms.ModelForm):
    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), label='Car Make')

    class Meta:
        model = CarModel
        fields = ['make', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class CarMakeForm(forms.ModelForm):
    class Meta:
        model = CarMake
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class CarClassForm(forms.ModelForm):
    class Meta:
        model = CarClass
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
        return [(year, year) for year in range(2000, current_year + 1)]


class CarForm(forms.ModelForm):
    year = forms.IntegerField(
        widget=SelectYearWidget(),
        label='Year',
        min_value=2000,
        max_value=datetime.now().year
    )

    mileage = forms.IntegerField(
        label='Mileage',
    )

    class Meta:
        model = Car
        fields = ['number_plate', 'make', 'model', 'year', 'color', 'daily_rate', 'weekly_rate', 'monthly_rate', 'seating_capacity', 'image', 'car_class', 'mileage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

        # Customize the "model" field's choices to display car model names in the form.
        car_models = CarModel.objects.all()
        self.fields['model'].queryset = car_models
        self.fields['model'].to_field_name = 'name'
        self.fields['model'].label_from_instance = lambda obj: obj.name  # Set custom label for model choices

        # Customize the "make" field's choices to display car make names in the form.
        car_makes = CarMake.objects.all()
        self.fields['make'].queryset = car_makes
        self.fields['make'].to_field_name = 'name'
        self.fields['make'].label_from_instance = lambda obj: obj.name  # Set custom label for make choices

        # Customize the "car_class" field's choices to display car class names in the form.
        car_classes = CarClass.objects.all()
        self.fields['car_class'].queryset = car_classes
        self.fields['car_class'].to_field_name = 'name'
        self.fields['car_class'].label_from_instance = lambda obj: obj.name  # Set custom label for car class choices

    
    
class CarServiceForm(forms.ModelForm):
    class Meta:
        model = CarService
        fields = [
            'car', 'service_date', 'service_report', 'cost', 'quantity', 'next_service', 'service_by', 'service_provider_contacts',
        ]
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
            'service_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'service_report': forms.Textarea(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'next_service': forms.TextInput(attrs={'class': 'form-control'}),
            'service_by': forms.TextInput(attrs={'class': 'form-control'}),
            'service_provider_contacts': forms.Textarea(attrs={'class': 'form-control'}),
        }
      




class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['car', 'insurance_company', 'policy_number', 'start_date', 'insurance_amount', 'duration']
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
            'insurance_company': forms.TextInput(attrs={'class': 'form-control'}),
            'policy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'insurance_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'car': 'Select Car',
            'insurance_company': 'Insurance Company',
            'policy_number': 'Policy Number',
            'start_date': 'Start Date',
            'insurance_amount': 'Insurance Amount',
            'duration': 'Insurance Duration',
        }

        duration_choices = Insurance.DURATION_CHOICES
        duration_choices.insert(0, ('', 'Select Duration'))
        widgets['duration'] = forms.Select(attrs={'class': 'form-control'}, choices=duration_choices)
