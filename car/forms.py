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
        return [(year, year) for year in range(1900, current_year + 1)]


class CarForm(forms.ModelForm):
    year = forms.IntegerField(
        widget=SelectYearWidget(),
        label='Year',
        min_value=1900,
        max_value=datetime.now().year
    )

    class Meta:
        model = Car
        fields = ['number_plate', 'make', 'model', 'year', 'color',  'daily_rate', 'weekly_rate', 'monthly_rate', 'seating_capacity', 'image', 'car_class']

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

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Ensure the uploaded image is not too large (limit to 5MB)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("The image size should be less than 5MB.")
        return image