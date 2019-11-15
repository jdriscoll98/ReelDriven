from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Client

class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SurveyForm(forms.ModelForm):
    # first_priority = forms.CharField(max_length=100)
    # second_priority = forms.CharField(max_length=100)
    # third_priority = forms.CharField(max_length=100)
    class Meta:
        model = Client
        fields = ('first_priority', 'second_priority', 'third_priority')