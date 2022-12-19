from django.shortcuts import render

from django.http import HttpResponse

from .models import Doctor, Patient, Study

def indexDoctors(request):
    doctors = Doctor.objects.all()[:5]
    output = '<br>'.join([el.doctor_name for el in doctors])
    return HttpResponse(output)

def indexPatients(request):
    patients = Patient.objects.all()[:5]
    output = '<br>'.join([el.patient_name for el in patients])
    return HttpResponse(output)