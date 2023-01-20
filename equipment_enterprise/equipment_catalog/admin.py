from django.contrib import admin

from .models import *

class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'surname', 'patronymic',)}


class EquipmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand', 'model',)}


class EquipmentCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Position)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentEmployee)