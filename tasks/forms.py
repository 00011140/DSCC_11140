from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'tags', 'completed']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            }),
        }

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
    }))