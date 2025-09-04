from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import *
from Ressource.models import Ressource

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    password = None 

    class Meta:
        model = User
        fields = ("username", "email")
        
        
class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ["titre", "fichier", "type"] 
