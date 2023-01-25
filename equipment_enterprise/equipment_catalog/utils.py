from .models import *

cats = EquipmentCategory.objects.all()
positions = Position.objects.all()

menu = [
    {'title': 'Оборудование', 'url_name': 'home'},
    {'title': 'Сотрудники', 'url_name': 'employees'},
    #{'title': 'Допустить сотрудника к оборудованию', 'url_name': 'add_equipment_employee'},
    #{'title': 'Размемтить оборудование', 'url_name': 'add_equipment_location'},
]