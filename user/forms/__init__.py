# forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class RegisterForm(forms.Form):
    c_username = forms.CharField(max_length=150, label="Username")
    c_email = forms.EmailField(label="Email")
    c_firstName = forms.CharField(max_length=50, label="First Name")
    c_lastName = forms.CharField(max_length=50, label="Last Name")
    c_password = forms.CharField(widget=forms.PasswordInput, label="Password")
    c_verify_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        c_password = cleaned_data.get("c_password")
        c_verify_password = cleaned_data.get("c_verify_password")

        if c_password != c_verify_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
