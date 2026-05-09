from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'unit_preference', 'timezone']


class UserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'unit_preference', 'timezone']
