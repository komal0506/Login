from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User


class LoginForm(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput)
    password = forms.IntegerField(widget = forms.PasswordInput)

class SignUp(UserCreationForm):
    firstname = forms.CharField(widget = forms.TextInput)
    lastname = forms.CharField(widget = forms.TextInput)
    username = forms.CharField(widget = forms.TextInput)   
    email = forms.EmailField(widget = forms.EmailInput)
    password = forms.IntegerField(widget = forms.PasswordInput)
    password2 = forms.IntegerField(widget = forms.PasswordInput)
    address = forms.CharField(widget = forms.TextInput)

class Meta:
    model = User
    fields = ('firstname','lastname','username','email','password','password1','is_patient','is_doctor')