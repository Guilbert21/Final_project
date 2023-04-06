from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']