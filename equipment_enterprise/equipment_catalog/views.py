from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView
from django.http import request, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *
from .utils import *
from .forms import *


class HomeView(DataMixin, ListView):
    model = Equipment
    template_name = 'equipment_catalog/index.html'
    context_object_name = 'equipment_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Главная страница', cats=cats, left_bar=EquipmentCategory.cat())
        return context | context_1


class EquipmentView(DataMixin, DetailView):
    model = Equipment
    template_name = 'equipment_catalog/equipment.html'
    context_object_name = 'equipment'
    slug_url_kwarg = 'equipment_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        eq = Equipment.objects.filter(slug=self.kwargs['equipment_slug'])
        context_1 = super().get_user_context(title=eq[0].brand + eq[0].model, cats=cats, left_bar=EquipmentCategory.cat())
        return context | context_1


class CategoryViews(DataMixin, ListView):
    model = Equipment
    template_name = 'equipment_catalog/index.html'
    context_object_name = 'equipment_list'
    slug_url_kwarg = 'category_slug'

    def get_queryset(self):
        return Equipment.objects.filter(category_id__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = list(EquipmentCategory.objects.filter(slug=self.kwargs['category_slug']))[0]
        context_1 = super().get_user_context(title=title, cats=cats, left_bar=EquipmentCategory.cat())
        return context | context_1


class EmployeesView(DataMixin, ListView):
    model = Employee
    template_name = 'equipment_catalog/employees.html'
    context_object_name = 'employees_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Сотрудники', cats=positions, left_bar=Position.cat())
        return context | context_1


class EmployeesPositionView(DataMixin, ListView):
    model = Employee
    template_name = 'equipment_catalog/employees.html'
    context_object_name = 'employees_list'
    slug_url_kwarg = 'position_slug'

    def get_queryset(self):
        return Employee.objects.filter(position_id__slug=self.kwargs['position_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = list(Position.objects.filter(slug=self.kwargs['position_slug']))[0]
        context_1 = super().get_user_context(title=title, cats=positions, left_bar=Position.cat())
        return context | context_1


class EmployeesViewDetail(DataMixin, DetailView):
    model = Employee
    template_name = 'equipment_catalog/employee.html'
    context_object_name = 'employee'
    slug_url_kwarg = 'employee_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        emp = Employee.objects.filter(slug=self.kwargs['employee_slug'])
        context_1 = super().get_user_context(title=emp[0], cats=positions, left_bar=Position.cat())
        return context | context_1


class CreateEmployeeView(DataMixin, CreateView):
    form_class = CreateEmployeeForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Добавить сотрудника', cats=positions, left_bar=Position.cat(), ur='add_employee')
        return context | context_1

    # def get(self, request):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()


class CreateEquipmentView(DataMixin, CreateView):
    form_class = CreateEquipmentForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Добавить оборудование', cats=cats, left_bar=EquipmentCategory.cat(), ur='add_equipment')
        return context | context_1


class CreateEquipmentEmployeeView(DataMixin, CreateView):
    form_class = CreateEquipmentEmployeeForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Допустить сотрудника к оборудованию', cats=cats, left_bar=Position.cat(), ur='add_equipment_emploee')
        return context | context_1

    def form_valid(self, form):
        EquipmentEmployee(**form.cleaned_data).save()
        return redirect('employees')


class CreateEquipmentLocationView(DataMixin, CreateView):
    form_class = CreateEquipmentLocationForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Разместить оборудование', cats=cats, left_bar=EquipmentCategory.cat(), ur='add_equipment_location')
        return context | context_1

    def form_valid(self, form):
        EquipmentLocation(**form.cleaned_data).save()
        return redirect('home')


class DeleteEmployeeView(DataMixin, DeleteView):
    model = Employee
    template_name = 'equipment_catalog/delete.html'
    slug_url_kwarg = 'employee_slug'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Удалить сотрудника', cats=positions, left_bar=Position.cat(), ur='delete_employee')
        return context | context_1

    def form_valid(self, form):
        Employee.objects.filter(slug=self.kwargs['employee_slug']).delete()
        return redirect('employees')


class DeleteEquipmentView(DataMixin, DeleteView):
    model = Equipment
    template_name = 'equipment_catalog/delete.html'
    slug_url_kwarg = 'equipment_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Удалить оборудование', cats=cats, left_bar=EquipmentCategory.cat(), ur='delete_equipment')
        return context | context_1

    def form_valid(self, form):
        Equipment.objects.filter(slug=self.kwargs['equipment_slug']).delete()
        return redirect('home')


class LoginUserView(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'equipment_catalog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Вход', cats=cats, left_bar=EquipmentCategory.cat())
        return context | context_1

    def get_success_url(self):
        return reverse_lazy('home')


class DeleteEquipmentLocationView(DataMixin, DeleteView):
    model = EquipmentLocation
    template_name = 'equipment_catalog/delete_equipment_location.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_1 = super().get_user_context(title='Удалить оборудование из цеха', cats=cats, left_bar=EquipmentCategory.cat())
        return context | context_1

    def form_valid(self, form):
        EquipmentLocation.objects.filter(id=self.kwargs['pk']).delete()
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')







