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
        return context

    def get_queryset(self):
        return Equipment.objects.all()

    def get_absolute_url(self):
        pass


class EquipmentView(DeleteView):
    model = Equipment
    template_name = 'equipment_catalog/equipment.html'





