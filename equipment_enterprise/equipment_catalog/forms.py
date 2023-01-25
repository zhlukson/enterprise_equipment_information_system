from django import forms
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
