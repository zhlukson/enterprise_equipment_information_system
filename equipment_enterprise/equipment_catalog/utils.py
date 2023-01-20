from .models import *

cats = EquipmentCategory.objects.all()

menu = [
    {'title': 'Оборудование', 'url_name': 'home'},
    {'title': 'Сотрудники', 'url_name': 'home'},
]