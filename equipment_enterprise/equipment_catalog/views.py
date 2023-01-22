from django.shortcuts import render
from django.views.generic import ListView, DeleteView
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
        return context


class EquipmentView(DeleteView):
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
        return context







