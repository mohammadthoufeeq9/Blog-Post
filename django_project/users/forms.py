from django import forms
from django.contrib.auth.models import User #Django's built-in authentication system
from django.contrib.auth.forms import UserCreationForm #Django's built-in authentication system

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model =User
        fields=['username','email','password1','password2']