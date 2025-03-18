from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor

class VendorRegistrationForm(UserCreationForm):
    class Meta:
        model = Vendor
        fields = ['username', 'email', 'password1', 'password2']