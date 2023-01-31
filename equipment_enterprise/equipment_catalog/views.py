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


class CreateEmployeeView(CreateView):
    form_class = CreateEmployeeForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить сотрудника'
        context['menu'] = menu
        context['cats'] = positions
        context['left_bar'] = Position.cat()
        context['ur'] = 'add_employee'
        return context

    # def get(self, request):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()


class CreateEquipmentView(CreateView):
    form_class = CreateEquipmentForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить оборудование'
        context['menu'] = menu
        context['cats'] = cats
        context['left_bar'] = EquipmentCategory.cat()
        context['ur'] = 'add_equipment'
        return context


class CreateEquipmentEmployeeView(CreateView):
    form_class = CreateEquipmentEmployeeForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Допустить сотрудника к оборудованию'
        context['menu'] = menu
        context['cats'] = cats
        context['left_bar'] = Position.cat()
        context['ur'] = 'add_equipment_emploee'
        return context

    def form_valid(self, form):
        EquipmentEmployee(**form.cleaned_data).save()
        return redirect('employees')


class CreateEquipmentLocationView(CreateView):
    form_class = CreateEquipmentLocationForm
    template_name = 'equipment_catalog/forms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Размемтить оборудование'
        context['menu'] = menu
        context['cats'] = cats
        context['left_bar'] = EquipmentCategory.cat()
        context['ur'] = 'add_equipment_location'
        return context

    def form_valid(self, form):
        EquipmentLocation(**form.cleaned_data).save()
        return redirect('home')


class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'equipment_catalog/delete.html'
    slug_url_kwarg = 'employee_slug'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить сотрудника'
        context['menu'] = menu
        context['cats'] = positions
        context['left_bar'] = Position.cat()
        context['ur'] = 'delete_employee'
        return context

    def form_valid(self, form):
        Employee.objects.filter(slug=self.kwargs['employee_slug']).delete()
        return redirect('employees')


class DeleteEquipmentView(DeleteView):
    model = Equipment
    template_name = 'equipment_catalog/delete.html'
    slug_url_kwarg = 'equipment_slug'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить оборудование'
        context['menu'] = menu
        context['cats'] = cats
        context['left_bar'] = EquipmentCategory.cat()
        context['ur'] = 'delete_equipment'
        return context

    def form_valid(self, form):
        Employee.objects.filter(slug=self.kwargs['equipment_slug']).delete()
        return redirect('home')


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'equipment_catalog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['menu'] = menu
        context['cats'] = cats
        context['left_bar'] = EquipmentCategory.cat()
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class DeleteEquipmentLocationView(DeleteView):
    model = EquipmentLocation
    template_name = 'equipment_catalog/delete_equipment_location.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить оборудование из цеха'
        context['menu'] = menu
        context['cats'] = cats
        context['left_bar'] = EquipmentCategory.cat()
        return context

    def form_valid(self, form):
        EquipmentLocation.objects.filter(id=self.kwargs['pk']).delete()
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')







