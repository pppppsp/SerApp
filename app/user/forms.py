from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User
from django import forms

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'patronymic', 'email', 'password1', 'password2']
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-indigo-500'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-indigo-500'
        })
    )
