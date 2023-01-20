from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipment/<slug:equipment_slug>/', EquipmentView.as_view(), name='equipment'),
]
