from django.contrib import admin
from doctors.models import Doctor

class MyAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "speciality", "added_date")

admin.site.register(Doctor, MyAdmin)

