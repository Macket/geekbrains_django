from django.forms import ModelForm
from django import forms
from .models import AdvUser, user_registrated
from datetime import date,timedelta,datetime
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.core import validators

#from django.shortcuts import render

class ChangeUserInfoForm(forms.ModelForm):
    today = date.today()
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    birstday = forms.DateField(label='Дата рождения',initial=today,widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name','sex','birstday','address','phone', 'send_messages')

class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput,
                help_text='Введите тот же самый пароль еще раз для проверки')

    

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        validate = password_validation.validate_password(password1)
        if validate:
            errors = {'password1': ValidationError('Введите другой пароль',
                                  code='password_mismatch')} 
            raise forms.ValidationError(errors)


        elif password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают',
                                  code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'send_messages')



    
