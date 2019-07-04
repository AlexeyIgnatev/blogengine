from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Profile


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mt-2', 'placeholder': 'Enter password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mt-2', 'placeholder': 'Repeat password'})

    class Meta(UserCreationForm.Meta):
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter username'})
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Enter username'}),
        self.fields['password'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Enter password'})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
