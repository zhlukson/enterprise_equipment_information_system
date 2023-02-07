from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['surname', 'name', 'patronymic', 'position_id', 'phone_number']


class CreateEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['brand', 'model', 'category', 'information_employee', 'additional_information', 'photo']


class CreateEquipmentEmployeeForm(forms.ModelForm):
    class Meta:
        model = EquipmentEmployee
        fields = ['equipment', 'employee']


class CreateEquipmentLocationForm(forms.ModelForm):
    class Meta:
        model = EquipmentLocation
        fields = ['location', 'equipment']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
