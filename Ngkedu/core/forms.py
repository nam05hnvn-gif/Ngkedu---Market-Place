from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full h-10 rounded p-4', 'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full h-10 rounded p-4', 'placeholder': 'Your Password'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full h-10 rounded p-4', 'placeholder': 'Your Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full h-10 rounded p-4', 'placeholder': 'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full h-10 rounded p-4', 'placeholder': 'Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full h-10 rounded p-4', 'placeholder': 'Confirm Password'}))