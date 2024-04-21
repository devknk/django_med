from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Doctor


def doctors(request):
    template = loader.get_template('doctors.html')
    all_doctors = Doctor.objects.all().values()
    context = {'all_doctors': all_doctors,}
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