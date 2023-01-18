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


class CNCLathe(models.Model):
    class Meta:
        verbose_name = 'Токарный станок с ЧПУ'
        verbose_name_plural = 'Токарные станки с ЧПУ'

    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    move_x = models.IntegerField(verbose_name='Перемещение по оси X, мм')
    move_y = models.IntegerField(verbose_name='Перемещение по оси Z, мм')
    spindle_speed = models.IntegerField(verbose_name='Обороты шпинделя, об/мин')
    number_of_positions = models.IntegerField(verbose_name='Количество позиций в револьверной головке')
    length = models.IntegerField(verbose_name='Длинна')
    width = models.IntegerField(verbose_name='Ширина')
    height = models.IntegerField(verbose_name='Высота')
    weight = models.IntegerField(verbose_name='Вес')
    additional_information = models.URLField(verbose_name='Дополнительная информация', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    location = models.CharField(max_length=255, verbose_name='Расположение')

    def __str__(self):
        return f'{self.brand} {self.model}'


class CNCLatheEmployee(models.Model):
    class Meta:
        verbose_name = 'Токарный станок с ЧПУ - Сотрудник'
        verbose_name_plural = 'Токарный станок с ЧПУ - Сотрудник'
        unique_together = ['cnc_lathe', 'employee']

    cnc_lathe = models.ForeignKey('CNCLathe', on_delete=models.PROTECT, verbose_name="Токарный станок с ЧПУ")
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name="Сотрудник, допущенный к работе")

    def __str__(self):
        return f'{self.cnc_lathe} - {self.employee}'