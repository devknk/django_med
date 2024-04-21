from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/details/<int:id>', views.details, name='details'),
    path('', views.index, name='index')
]