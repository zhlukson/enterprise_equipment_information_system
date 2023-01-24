from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .utils import *


class HomeView(ListView):
    model = Equipment
    template_name = 'equipment_catalog/index.html'
    context_object_name = 'equipment_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cats'] = cats
        context['menu'] = menu
        context['left_bar'] = EquipmentCategory.cat()
        return context


class PositionsView(ListView):
    model = Employee
    template_name = 'equipment_catalog/employees.html'
    context_object_name = 'employees_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = positions
        context['title'] = 'Сотрудники'
        context['left_bar'] = Position.cat()
        return context


class EquipmentView(DetailView):
    model = Equipment
    template_name = 'equipment_catalog/equipment.html'
    context_object_name = 'equipment'
    slug_url_kwarg = 'equipment_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        eq = Equipment.objects.filter(slug=self.kwargs['equipment_slug'])
        context['title'] = eq[0].brand + eq[0].model
        context['cats'] = cats
        context['menu'] = menu
        context['left_bar'] = EquipmentCategory.cat()
        return context


class CategoryViews(ListView):
    model = Equipment
    template_name = 'equipment_catalog/index.html'
    context_object_name = 'equipment_list'
    slug_url_kwarg = 'category_slug'

    def get_queryset(self):
        return Equipment.objects.filter(category_id__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = cats
        context['title'] = list(EquipmentCategory.objects.filter(slug=self.kwargs['category_slug']))[0]
        context['left_bar'] = EquipmentCategory.cat()
        return context


class EmployeesView(ListView):
    model = Employee
    template_name = 'equipment_catalog/employees.html'
    context_object_name = 'employees_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = positions
        context['title'] = 'Сотрудники'
        context['left_bar'] = Position.cat()
        return context


class EmployeesPositionView(ListView):
    model = Employee
    template_name = 'equipment_catalog/employees.html'
    context_object_name = 'employees_list'
    slug_url_kwarg = 'position_slug'

    def get_queryset(self):
        return Employee.objects.filter(position_id__slug=self.kwargs['position_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = positions
        context['title'] = list(Position.objects.filter(slug=self.kwargs['position_slug']))[0]
        context['left_bar'] = Position.cat()
        return context


class EmployeesViewDetail(DetailView):
    model = Employee
    template_name = 'equipment_catalog/employee.html'
    context_object_name = 'employee'
    slug_url_kwarg = 'employee_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        emp = Employee.objects.filter(slug=self.kwargs['employee_slug'])
        context['title'] = emp[0]
        context['menu'] = menu
        context['cats'] = positions
        context['left_bar'] = Position.cat()
        return context









