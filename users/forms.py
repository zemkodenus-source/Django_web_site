from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserRegForm(UserCreationForm):
    username = forms.CharField(
        label='Створіть Nickname',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nickname',
        })
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш Email',
        })
    )

    password1 = forms.CharField(
        label='Створіть пароль',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Створіть Password',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Створіть Nickname',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nickname',
        })
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш Email',
        })
    )
    class Meta:
        model = User
        fields = ('username', 'email')