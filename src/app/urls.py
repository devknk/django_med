from django.urls import path
from . import views

urlpatterns = [
    path('reservations/reservation/<int:id>', views.reservation, name='reservation'),
    path('reservations/', views.reservations, name='reservations'),
    path('doctors/', views.doctors, name='doctors'),
    path('specialities/', views.specialities_list, name='specialities'),
    path('doctors/details/<int:id>', views.details, name='details'),
    path('specialities/speciality/details/<int:id>', views.details, name='details'),
    path('specialities/speciality/<str:speciality>', views.one_speciality_list, name='spec_list'),
    path('', views.index, name='index')
]