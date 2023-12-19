from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text='A valid email address, please.',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='')
    


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'email', 'id_number', 'local_address', 'home_address', 'company',
                  'nationality', 'age', 'drivers_license_number', 'country_of_issue', 'license_expiry',
                  'credit_card', 'credit_card_number', 'card_expiry', 'physical_address', 'phone_number',
                  'office_telephone', 'residence_address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Number'}),
            'local_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Local Address'}),
            'home_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Address'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'drivers_license_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Driver's License Number"}),
            'country_of_issue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country of Issue'}),
            'license_expiry': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'credit_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Credit Card'}),
            'credit_card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Credit Card Number'}),
            'card_expiry': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'physical_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Physical Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'office_telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Office Telephone'}),
            'residence_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residence Address'}),
        }
      

    # Override field definitions to make certain fields not required
    first_name = forms.CharField(required=False)
    id_number = forms.IntegerField(required=False)  
    age = forms.IntegerField(required=False)  
    email = forms.EmailField(required=False)  
    local_address = forms.CharField(required=False)  
    home_address = forms.CharField(required=False)  
    company = forms.CharField(required=False) 
    nationality = forms.CharField(required=False) 
    country_of_issue = forms.CharField(required=False)  
    license_expiry = forms.DateField(required=False)  
    credit_card = forms.CharField(required=False)  
    credit_card_number = forms.CharField(required=False)  
    card_expiry = forms.DateField(required=False)  
    physical_address = forms.CharField(required=False)  
    phone_number = forms.CharField(required=False)  
    office_telephone = forms.CharField(required=False)  
    residence_address = forms.CharField(required=False)  

    labels = {
            'first_name': 'Name',
        }
