from django.core.exceptions import ValidationError

from .models import User
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder':'Логин'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder':'Введите email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-input','placeholder':'Введите логин'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-input','placeholder':'Введите пароль'}))


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))