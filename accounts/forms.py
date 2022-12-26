from django import forms
from .models import User
from .validators import phone_number_validator


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11,validators=[phone_number_validator])
    password = forms.CharField(max_length=128)


class RegisterForm(forms.Form):
    phone_number = forms.CharField(max_length=11, validators=[phone_number_validator])
    password = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "passwords do not match",
                code='password_mismatch',
            )
        return password2

    def clean_phone_number(self):
        data = self.cleaned_data
        phone_number = data.get("phone_number")
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise forms.ValidationError(
                "we have this phone number on database", code="duplicate")
        return phone_number

class LoginRequestForm(forms.Form):
    phone_number = forms.CharField(max_length=11, validators=[phone_number_validator])

class OTPConfirmForm(LoginRequestForm):
    otp_code = forms.CharField(max_length=5)