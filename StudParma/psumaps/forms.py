from django.contrib.auth.forms import UserCreationForm

from .models import UsersModel
from django.forms import ModelForm, TextInput


class UsersRegForm(ModelForm):
    class Meta:
        model = UsersModel
        fields = ['name', 'surname', 'login', 'password']

        # Словарь с html-разметкой
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }

class UsersLoginForm(ModelForm):
    class Meta:
        model = UsersModel
        fields = ['login', 'password']

        # Словарь с html-разметкой
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }