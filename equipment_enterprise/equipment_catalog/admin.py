from django.contrib import admin

from .models import *

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(EquipmentCategory)
admin.site.register(Equipment)
admin.site.register(EquipmentEmployee)