from django.db import models
from django.core.validators import validate_email
from django.utils import timezone


class Doctor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    second_name = models.CharField(max_length=255, blank = True, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    speciality = models.CharField(max_length=255, blank=False, null=True)
    added_date = models.DateField(auto_now_add=True)
    phone = models.IntegerField(unique=True, blank=False, null=False)
    email = models.EmailField(max_length=254, verbose_name="Email Address", unique=True, validators=[validate_email])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
