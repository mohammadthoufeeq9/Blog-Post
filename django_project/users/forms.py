from django import forms
from django.contrib.auth.models import User #Django's built-in authentication system
from django.contrib.auth.forms import UserCreationForm #Django's built-in authentication system
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model =User
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']