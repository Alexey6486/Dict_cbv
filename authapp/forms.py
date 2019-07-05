from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, models
from django.forms import models

from .models import DictUser

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Your login'
        }
    ))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Your password'
        }
    ))


class RegistrationForm(UserCreationForm): #здесь буде пользовать заготовку, т.к. так делают почти везде, как задавать
    #два поля пароль на проверку не нашел

    class Meta:
        model = DictUser
        fields = ('username', 'password1', 'password2', 'email')

    #задать плейс отдельно каждому полю, затем все инпутам одинаковый класс
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'your nickname'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['email'].widget.attrs['placeholder'] = 'your email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'