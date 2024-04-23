from django.contrib import admin
from app.models import Doctor, Patient, Visit


class MyDoctors(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "speciality", "added_date")

class MyVisits(admin.ModelAdmin):
    list_display = ("id", "date", "doctor", "patient", "created_date")

class MyPatients(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "added_date")


admin.site.register(Doctor, MyDoctors)
admin.site.register(Patient, MyPatients)
admin.site.register(Visit, MyVisits)
