import json
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Position(models.Model):
    class Meta:
        verbose_name = ' Должность'
        verbose_name_plural = 'Должности'

    name = models.CharField(max_length=100, verbose_name='Название должности')

    def __str__(self):
        return self.name


class Employee(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True)
    position_id = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    phone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона', unique=True, null=False, blank=False)

    def __str__(self):
        if self.patronymic is not None:
            p = self.patronymic
        else:
            p = ''
        return f'{self.name} {self.patronymic} {self.surname}'


class EquipmentCategory(models.Model):
    class Meta:
        verbose_name = 'Категория оборудования'
        verbose_name_plural = 'Категории оборудования'

    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Equipment(models.Model):
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель', null=True)
    category = models.ForeignKey('EquipmentCategory', on_delete=models.PROTECT, verbose_name='Категория')
    information_employee = models.FileField(upload_to='description_equipment/%Y/%m/%d/', verbose_name='Характеристики')
    additional_information = models.URLField(verbose_name='Дополнительная информация', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    location = models.CharField(max_length=255, verbose_name='Расположение')

    def __str__(self):
        return f'{self.brand} {self.model}'

    @property
    def information(self):
        with open('.' + self.information_employee.url) as file_1:
            return json.load(file_1)


class EquipmentEmployee(models.Model):
    class Meta:
        verbose_name = 'Оборудование - Сотрудник'
        verbose_name_plural = 'Оборудование - Сотрудник'
        unique_together = ['equipment', 'employee']

    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT, verbose_name="Оборудование")
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name="Сотрудник, допущенный к работе")

    def __str__(self):
        return f'{self.equipment} - {self.employee}'