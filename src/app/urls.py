from django.urls import path
from django.contrib import admin
from . import views
from account.views import (
    register_view
)

urlpatterns = [
    path('reservations/reservation/<int:id>', views.single_reservation_view, name='reservation'),
    path('reservations/', views.reservations_view, name='reservations'),
    path('visits/', views.visits_view, name='available_visits'),
    path('visits/visit/<int:id>', views.visit_view, name='available_visit'),
    # path('visits/visit/<int:id>', views.book_visit, name='book_visit'),
    # path('visits/visit_booked/<int:id>', views.visit_booked_view, name='visit_booked'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('specialities/', views.specialities_list_view, name='specialities'),
    path('doctors/details/<int:id>', views.doctors_details_view, name='details'),
    path('specialities/speciality/details/<int:id>', views.doctors_details_view, name='details'),
    path('specialities/speciality/<str:speciality>', views.one_speciality_view, name='spec_list'),
    path('account/register/', register_view, name='register'),
    path('', views.index_view, name='index'),
]