from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Doctor, Visit
from django.db.models import Q


def doctors(request):
    template = loader.get_template('doctors.html')
    all_doctors = Doctor.objects.all().values()
    context = {'all_doctors': all_doctors, }
    return HttpResponse(template.render(context, request))


def details(request, id):
    doctor = Doctor.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'doctor': doctor,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def visits(request):
    available_visits = Visit.objects.filter(patient__isnull=True)
    template = loader.get_template('visits.html')
    context = {'available_visits': available_visits}
    return HttpResponse(template.render(context, request))


def visit(request, id):
    visit = Visit.objects.get(id=id)
    template = loader.get_template('visit.html')
    context = {'visit': visit}
    return HttpResponse(template.render(context, request))


# visits that have been booked by patients:
def reservations(request):
    all_reservations = Visit.objects.filter(patient__isnull=False)
    template = loader.get_template('reservations.html')
    context = {'all_reservations': all_reservations}
    return HttpResponse(template.render(context, request))


def reservation(request, id):
    reservation = Visit.objects.get(id=id)
    template = loader.get_template('reservation.html')
    context = {
        'reservation': reservation,
    }
    return HttpResponse(template.render(context, request))


def specialities_list(request):
    template = loader.get_template('specialities.html')
    # unique_specialities = Doctor.objects.filter('speciality', flat=True).distinct() to zwraca liste zamaist slownika!
    unique_specialities = Doctor.objects.values('speciality').distinct()
    context = {'specialities': unique_specialities}
    return HttpResponse(template.render(context, request))


def one_speciality_list(request, speciality):
    template = loader.get_template('speciality.html')
    spec_list = Doctor.objects.filter(speciality=speciality).values()
    context = {'spec_list': spec_list, 'speciality': speciality}
    return HttpResponse(template.render(context, request))
