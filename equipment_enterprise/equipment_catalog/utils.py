from .models import *

cats = EquipmentCategory.objects.all()
positions = Position.objects.all()

menu = [
    {'title': 'Оборудование', 'url_name': 'home'},
    {'title': 'Сотрудники', 'url_name': 'employees'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context