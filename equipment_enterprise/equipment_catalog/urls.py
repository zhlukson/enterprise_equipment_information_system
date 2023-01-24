from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipments/<slug:category_slug>/<slug:equipment_slug>/', EquipmentView.as_view(), name='equipments'),
    path('equipments/<slug:category_slug>/', CategoryViews.as_view(), name='category'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employees/<slug:position_slug>/', EmployeesPositionView.as_view(), name='positions'),
    path('employees/<slug:position_slug>/<slug:employee_slug>/', EmployeesViewDetail.as_view(), name='employee_detail'),
]
