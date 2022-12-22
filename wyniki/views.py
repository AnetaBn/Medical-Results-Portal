import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from legacy.models import Doctor, Patient, Study
# from .models import Doctor, Patient, Study

def home(request):
    return render(request, "wyniki/home.html")

def about(request):
    return render(request, "wyniki/about.html")

def hello_there(request, name):
    return render(
        request,
        'wyniki/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def add_results(request, name):
    return render(
        request,
        'wyniki/add_results.html',
        {
            # 'name': name,
            'msg': name
        }
    )


def create_study(request, name):
    if request.method == 'POST':
        if request.POST.get('patient_id') and request.POST.get('hospital') and request.POST.get('date') and request.POST.get('type'):
            one_study=Study()
            one_study.hospital = request.POST.get('hospital')
            one_study.study_date = request.POST.get('date')
            one_study.modality = request.POST.get('type')
            one_study.patient = Patient.objects.get(patient_id = request.POST.get('patient_id'))
            one_study.doctor = Doctor.objects.get(doctor_name = 'John Watson') # to change 
            one_study.save()
            msge ="Data inserted to study table with id: " + str(one_study.study_id)
        else:
            msge=name
    else:
        msge=name

    return render(request,'wyniki/add_results.html',
        {
            'msg': msge,
        }
    )

# HOW TO DELETE - USEFUL COMMAND!!!
# https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
