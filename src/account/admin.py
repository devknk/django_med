from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
# from app.models import Doctor, Patient, Visit
from app.models import Doctor, Visit



class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class MyDoctors(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "speciality", "added_date")


class MyVisits(admin.ModelAdmin):
    list_display = ("id", "date", "doctor", "patient", "created_date")
    readonly_fields = ["created_date", "speciality"]


# class MyPatients(admin.ModelAdmin):
#     list_display = ("id", "first_name", "last_name", "added_date")


admin.site.register(Account, AccountAdmin)

admin.site.register(Doctor, MyDoctors)
# admin.site.register(Patient, MyPatients)
admin.site.register(Visit, MyVisits)
