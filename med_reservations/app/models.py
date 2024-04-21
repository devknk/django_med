from django.db import models
from django.core.validators import validate_email
from django.utils import timezone
import uuid


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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(Member):
    identity_number = models.PositiveIntegerField(blank=False, null=False, unique=True)
    client_number = models.CharField(max_length=10, unique=True, default=generate_unique_client_number,
                                     verbose_name="Client Number")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    created_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reservations')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    description = models.TextField()

    # def __str__(self):
    #     return f"Reservation for {self.client.username} on {self.date}"
