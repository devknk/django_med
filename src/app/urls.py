from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('reservations/reservation/<int:visit_id>', views.single_reservation_view, name='reservation'),
    path('reservations/', views.reservations_view, name='reservations'),
    path('visits/', views.visits_view, name='available_visits'),
    path('my_visits/', views.my_visits_view, name='my_visits'),
    path('my_visits/visit/<int:visit_id>', views.visit_view, name='my_visits'),
    path('visits/visit/<int:visit_id>', views.visit_view, name='visit'),
    path('book_visit/<int:visit_id>', views.book_visit, name='book_visit'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('specialities/', views.specialities_list_view, name='specialities'),
    path('doctors/details/<int:id>', views.doctors_details_view, name='details'),
    path('specialities/speciality/details/<int:id>', views.doctors_details_view, name='details'),
    path('specialities/speciality/<str:speciality>', views.one_speciality_view, name='spec_list'),
    path('', views.index_view, name='index'),

]