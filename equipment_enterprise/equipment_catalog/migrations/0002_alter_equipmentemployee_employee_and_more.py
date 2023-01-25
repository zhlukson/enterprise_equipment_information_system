# Generated by Django 4.1.5 on 2023-01-25 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentemployee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment_catalog.employee', verbose_name='Сотрудник, допущенный к работе'),
        ),
        migrations.AlterField(
            model_name='equipmentemployee',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment_catalog.equipment', verbose_name='Оборудование'),
        ),
        migrations.AlterField(
            model_name='equipmentlocation',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment_catalog.equipment', verbose_name='Оборудование'),
        ),
        migrations.AlterField(
            model_name='equipmentlocation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment_catalog.workshops', verbose_name='Расположение'),
        ),
    ]
