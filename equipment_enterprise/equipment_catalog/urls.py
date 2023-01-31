from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('add-equipment-employee/', CreateEquipmentEmployeeView.as_view(), name='add_equipment_employee'),
    path('add-equipment-location/', CreateEquipmentLocationView.as_view(), name='add_equipment_location'),
    path('delete_equipment_location/<int:pk>/', DeleteEquipmentLocationView.as_view(), name='delete_equipment_location'),
    path('equipments/add-equipment/', CreateEquipmentView.as_view(), name='add_equipment'),
    path('equipments/<slug:category_slug>/<slug:equipment_slug>/', EquipmentView.as_view(), name='equipments'),
    path('equipments/<slug:category_slug>/<slug:equipment_slug>/delete/', DeleteEquipmentView.as_view(), name='delete_equipment'),
    path('equipments/<slug:category_slug>/', CategoryViews.as_view(), name='category'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employees/add-employee/', CreateEmployeeView.as_view(), name='add_employee'),
    path('employees/<slug:position_slug>/', EmployeesPositionView.as_view(), name='positions'),
    path('employees/<slug:position_slug>/<slug:employee_slug>/', EmployeesViewDetail.as_view(), name='employee_detail'),
    path('employees/<slug:position_slug>/<slug:employee_slug>/delete/', DeleteEmployeeView.as_view(), name='delete_employee'),

]
