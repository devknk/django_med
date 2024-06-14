import datetime

from django.db import models
from django.core.validators import validate_email
from django.utils import timezone
import uuid
from account.models import Account


def generate_unique_client_number():
    """
    Generate a unique client number using UUID.
    """
    return str(uuid.uuid4().int)[:10]


class Member(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    added_date = models.DateField(auto_now_add=True)
    phone = models.IntegerField(unique=True, blank=False, null=False)
    email = models.EmailField(max_length=254, verbose_name="Email Address", unique=True, validators=[validate_email])

    class Meta:
        abstract = True


class Doctor(Member):
    speciality = models.CharField(max_length=255, blank=False, null=True)
    info = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Lekarze"


class Visit(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='reservations', blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reservations')
    speciality = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField()
    description = models.TextField()
    is_booked = models.BooleanField(default=False)

    def add_patient(self, user):
        if not self.is_booked:
            self.patient = user
            self.is_booked = True
            self.save()
            return True
        return False

    def save(self, *args, **kwargs):
        if not self.speciality:
            self.speciality = self.doctor.speciality
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"Reservation for {self.patient.username} on {self.date}"

    class Meta:
        verbose_name_plural = "Wizyty"

    def is_past(self):
        return self.date < timezone.now() - datetime.timedelta(days=1)
