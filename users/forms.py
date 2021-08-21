from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm

from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Username or Password")


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address',
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    name = forms.CharField(max_length=60,
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text='Password must contain at least 8 character',
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text='Enter the same password as before',
    )
    check = forms.BooleanField(required=True)

    class Meta:
        model = UserModel
        fields = ("name", "email", "password1", "password2", "check")


class EditProfileForm(ModelForm):
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    image = forms.ImageField(
        required=False,
        error_messages={'invalid': "Image files only"},
        widget=forms.FileInput,
    )

    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['user']


class AccountInformationForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('name', 'email')
