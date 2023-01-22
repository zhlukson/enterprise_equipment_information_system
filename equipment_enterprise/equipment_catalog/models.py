import json
from django.db import models
from django.urls import reverse
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
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    position_id = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    phone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона', unique=True, null=False, blank=False)

    def __str__(self):
        if self.patronymic is not None:
            p = self.patronymic
        else:
            p = ''
        return f'{self.name} {self.patronymic} {self.surname}'

    def get_absolute_url(self):
        return reverse('employee', kwargs={'employee_slug': self.slug})


class EquipmentCategory(models.Model):
    class Meta:
        verbose_name = 'Категория оборудования'
        verbose_name_plural = 'Категории оборудования'

    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Equipment(models.Model):
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey('EquipmentCategory', on_delete=models.PROTECT, verbose_name='Категория')
    information_employee = models.FileField(upload_to='description_equipment/%Y/%m/%d/', verbose_name='Характеристики')
    additional_information = models.URLField(verbose_name='Дополнительная информация', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_absolute_url(self):
        return reverse('equipment', kwargs={'equipment_slug': self.slug})

    @property
    def information(self):
        with open('.' + self.information_employee.url) as file_1:
            return json.load(file_1)

    @property
    def equipment_employee(self):
        return [i.employee for i in EquipmentEmployee.objects.filter(equipment=self.pk)]


class EquipmentEmployee(models.Model):
    class Meta:
        verbose_name = 'Оборудование - Сотрудник'
        verbose_name_plural = 'Оборудование - Сотрудник'
        unique_together = ['equipment', 'employee']

    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT, verbose_name="Оборудование")
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name="Сотрудник, допущенный к работе")

    def __str__(self):
        return f'{self.equipment} - {self.employee}'


class Production(models.Model):
    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'

    production_name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.production_name

class Workshops(models.Model):
    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'

    number = models.IntegerField(verbose_name='Номер цеха', primary_key=True)
    production = models.ForeignKey('Production', on_delete=models.PROTECT, verbose_name='Производство')

    def __str__(self):
        return f'{self.production} производство, {self.number} цех'


class EquipmentLocation(models.Model):
    class Meta:
        verbose_name = 'Оборудование - Расположение'
        verbose_name_plural = 'Оборудование - Расположение'
        unique_together = ['location', 'equipment']

    location = models.ForeignKey('Workshops', on_delete=models.PROTECT, verbose_name='Расположение')
    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT, verbose_name='Оборудование')

    def __str__(self):
        return f'{self.equipment} --> {self.location}'


