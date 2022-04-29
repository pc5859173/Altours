"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
#import ugettext_lazy from django

# Import the following modules

class registerAlt(forms.Form):
    email = forms.CharField(
        max_length=20)
    password = forms.CharField(
        max_length=20
    )
    password_confirmation =forms.CharField(
        max_length=20
    )



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
