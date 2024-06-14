from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Doctor, Visit
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone


def doctors_view(request):
    template = loader.get_template('doctors.html')
    all_doctors = Doctor.objects.all().values()
    context = {'all_doctors': all_doctors, }
    return HttpResponse(template.render(context, request))


def doctors_details_view(request, id):
    doctor = Doctor.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'doctor': doctor,
    }
    return HttpResponse(template.render(context, request))


def index_view(request):
    template = loader.get_template('index.html')
    context = {'user': request.user}
    return HttpResponse(template.render(context, request))


def visits_view(request):
    available_visits = Visit.objects.filter(patient__isnull=True).order_by("doctor")
    future_visits = [available_visit for available_visit in available_visits if not available_visit.is_past()]
    template = loader.get_template('visits.html')
    context = {'future_visits': future_visits}
    return HttpResponse(template.render(context, request))


@login_required
def my_visits_view(request):
    my_visits = Visit.objects.filter(patient=request.user, date__gt=timezone.now()).order_by("-date")
    template = loader.get_template('my_visits.html')
    context = {'my_visits': my_visits}
    return HttpResponse(template.render(context, request))


@login_required
def my_past_visits_view(request):
    my_past_visits = Visit.objects.filter(patient=request.user, date__lt=timezone.now()).order_by("-date")
    template = loader.get_template('my_visits.html')
    context = {'my_past_visits': my_past_visits}
    return HttpResponse(template.render(context, request))


def visit_view(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    template = loader.get_template('visit.html')
    context = {'visit': visit}
    return HttpResponse(template.render(context, request))


@login_required
def book_visit(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    doctor = visit.doctor
    template = loader.get_template('reservation.html')
    patient = request.user
    visit.add_patient(patient)
    context = {
        'visit_id': visit_id,
        'visit': visit,
        'doctor': doctor,
    }
    return HttpResponse(template.render(context, request))


# visits that have been booked by patients, for future use:
@login_required
def reservations_view(request):
    all_reservations = Visit.objects.filter(patient__isnull=False)
    template = loader.get_template('reservations.html')
    context = {'all_reservations': all_reservations}
    return HttpResponse(template.render(context, request))


@login_required
def single_reservation_view(request, visit_id):
    reservation = Visit.objects.get(id=visit_id)
    template = loader.get_template('reservation.html')
    doctor = reservation.doctor
    context = {
        'reservation': reservation,
        'doctor': doctor,
    }
    return HttpResponse(template.render(context, request))


def specialities_list_view(request):
    template = loader.get_template('specialities.html')
    # unique_specialities = Doctor.objects.filter('speciality', flat=True).distinct() to zwraca liste zamaist slownika!
    unique_specialities = Doctor.objects.values('speciality').distinct()
    context = {'specialities': unique_specialities}
    return HttpResponse(template.render(context, request))


def one_speciality_view(request, speciality):
    template = loader.get_template('speciality.html')
    spec_list = Doctor.objects.filter(speciality=speciality).values()
    context = {'spec_list': spec_list, 'speciality': speciality}
    return HttpResponse(template.render(context, request))
