from django.contrib import admin
from app.models import Doctor, Patient, Reservation


class MyAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "speciality", "added_date")

class MyReservations(admin.ModelAdmin):
    list_display = ("id", "date", "doctor", "patient", "created_date")

class MyPatients(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "added_date")


admin.site.register(Doctor, MyAdmin)
admin.site.register(Patient, MyPatients)
admin.site.register(Reservation, MyReservations)
