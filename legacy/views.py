from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Patient, Study

def indexDoctors(request):
    doctors = Doctor.objects.all()
    output = '<br>'.join([el.doctor_name for el in doctors])
    return HttpResponse(output)

def indexPatients(request):
    patients = Patient.objects.all()
    output = '<br>'.join([el.patient_name for el in patients])
    return HttpResponse(output)

def modalities(request):
    studies = Study.objects.all()
    output = '<br>'.join([el.modality for el in studies])
    return HttpResponse(output)

# https://stackoverflow.com/questions/55652043/django-save-method-in-a-different-database