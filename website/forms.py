from django.contrib.auth import forms
from django.contrib.auth.models import User

class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)
    password_confirm = forms.CharField(max_length=200, required=True)
    phone_number = forms.IntegerField(max_length=9, required=True)

    def clean_password(self, form):
        data = form.cleaned_data()
        if data['password'] != data['password2']:
            raise ValidationError("Passwords must match")

    def save(self):
        data = self.cleaned_data()
        new_client = User(first_name = data.first_name, last_name=data.last_name)
        new_client.save()
        return super().save()

