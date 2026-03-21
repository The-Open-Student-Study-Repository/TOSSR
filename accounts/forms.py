from django import forms
from django.utils import timezone
from django_tomselect.app_settings import TomSelectConfig
from django_tomselect.forms import TomSelectModelChoiceField

from .models import User

class SignUpStep1Form(forms.Form):
    """Basic credentials to validate user can create account"""
    username = forms.CharField(
        max_length=150,
        help_text='Choose a username',
    )

    email = forms.EmailField(
        max_length=255,
        help_text='Your university email address',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        min_length=8,
        help_text='At least an 8 char password',
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirm Password',
    )

    privacy_accepted = forms.BooleanField(
        required=True,
        label="I accept the Privacy Policy",
        error_messages={'required': "You must agree to the Privacy Policy. before creating an account."},
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username has been taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already been registered to an account.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match. Please choose a different one.")

        return cleaned_data

class SignUpStep2Form(forms.Form):
    """
    Step 2: Student details
    """
    forename = forms.CharField(
        max_length=255,
        help_text='Forename',
    )

    surname = forms.CharField(
        max_length=255,
        help_text='Surname',
    )

    degree = TomSelectModelChoiceField(
        config=TomSelectConfig(
            url="accounts:degree_autocomplete",
            value_field="code",
            label_field="name",
            placeholder="Search your degree...",
            highlight=True,
            max_options=10,
        )
    )

    graduation_year = forms.IntegerField(
        min_value=timezone.now().year,
        max_value=timezone.now().year+6,
        help_text='Expected to graduate',
    )

    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        max_length=255,
        required=False,
        label='Bio',
        help_text='Tell us about yourself! (optional)',
    )


