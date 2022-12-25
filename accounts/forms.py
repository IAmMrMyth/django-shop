from django import forms


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(max_length=128)
