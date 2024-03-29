from django import forms
from .models import *
from django.forms import inlineformset_factory


class DamageImageForm(forms.ModelForm):
    class Meta:
        model = DamageImage
        fields = ['d_image']


InspectionDamageImageFormSet = inlineformset_factory(
    Inspection, DamageImage, form=DamageImageForm, extra=1
)


class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Inspection Date', 'required': False}),
            'car': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select car'}),
            'current_mileage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mileage EX.23', 'id': 'current_mileage'}),
            'service_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Tag EX. 23', 'id': 'service_tag'}),
            'next_service_due': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Due EX. 23', 'id': 'next_service_due'}),
            'insurance_expiry': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Inspection Date', 'required': False}),
            'fuel_tank_level': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': 0, 'max': 100, 'step': 1,  'id': 'fuelTankSlider', }),
            'emergency_equipment': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'oil_level': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'brake_fluid': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'power_steering_fluid': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'clutch_fluid': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'auto_transmission_fluid': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'radiator_fluid_level': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'windshield_washer_level': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'voltage_recorded': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter voltage recorded'}),
            'terminals_checked_and_tightened': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'battery_fluid': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'headlights_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'high_beam_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'brake_lights_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'indicators_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'reverse_lights_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'fog_lights_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'fr_tire_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Front right tire brand', 'label': ''}),
            'fr_tire_condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Front right tire condition', 'label': ''}),
            'fl_tire_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Front left tire brand', 'label': ''}),
            'fl_tire_condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Front left tire condition', 'label': ''}),
            'rr_tire_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rear right tire brand', 'label': ''}),
            'rr_tire_condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rear right tire condition', 'label': ''}),
            'rl_tire_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rear left tire brand', 'label': ''}),
            'rl_tire_condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rear left tire condition', 'label': ''}),
            'spare_tire_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spare tire brand', 'label': ''}),
            'spare_tire_condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spare tire condition', 'label': ''}),
            'warning_lights': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'air_conditioning_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'radio_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'CD': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'USB': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'AUX': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'FM_Expander': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'windscreen_condition': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'wipers_working': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'seat_belts_functioning': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'electric_mirrors_functioning': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'electric_windows_functioning': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Drivers first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Drivers last name'}),
            'inspectors_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inspector\'s first name'}),
            'inspectors_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inspector\'s last name'}),
            'additional_comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter additional comments'}),
            'dashboard_image': forms.FileInput(attrs={'class': 'form-control'}),
            'car_damage_images': forms.FileInput(attrs={'class': 'form-control', 'id': 'carDamageImages'}),

        }

        labels = {
            'date': '',
            'car': '',
            'current_mileage': '',
            'service_tag': '',
            'next_service_due': '',
            'insurance_expiry': '',
            'fuel_tank_level': '',
            'oil_level': '',
            'brake_fluid': '',
            'power_steering_fluid': '',
            'clutch_fluid': '',
            'auto_transmission_fluid': '',
            'radiator_fluid_level': '',
            'windshield_washer_level': '',
            'voltage_recorded': '',
            'terminals_checked_and_tightened': '',
            'battery_fluid': '',
            'headlights_working': '',
            'high_beam_working': '',
            'brake_lights_working': '',
            'indicators_working': '',
            'reverse_lights_working': '',
            'fog_lights_working': '',
            'fr_tire_brand': '',
            'fr_tire_condition': '',
            'fl_tire_brand': '',
            'fl_tire_condition': '',
            'rr_tire_brand': '',
            'rr_tire_condition': '',
            'rl_tire_brand': '',
            'rl_tire_condition': '',
            'spare_tire_brand': '',
            'spare_tire_condition': '',
            'warning_lights': '',
            'emergency_equipment': '',
            'air_conditioning_working': '',
            'radio_working': '',
            'CD': '',
            'USB': '',
            'AUX': '',
            'FM_Expander': '',
            'windscreen_condition': '',
            'wipers_working': '',
            'seat_belts_functioning': '',
            'electric_mirrors_functioning': '',
            'electric_windows_functioning': '',
            'first_name': '',
            'last_name': '',
            'drivers_signature': '',
            'inspectors_first_name': '',
            'inspectors_last_name': '',
            'inspectors_signature': '',
            'additional_comments': '',
            'dashboard_image': '',
            'car_damage_images': '',
        }

    def __init__(self, *args, **kwargs):
        super(InspectionForm, self).__init__(*args, **kwargs)
        self.fields['car'].empty_label = 'Select Vehicle'
