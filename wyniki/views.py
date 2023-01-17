from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from legacy.models import Doctor, Patient, Study
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
import os
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

def register_patient(request):
    return render(request, "wyniki/register_patient.html"
    )

def register_doctor(request):
    return render(request, "wyniki/register_doctor.html"
)


def add_results(request, name):
    return render(
        request,
        'wyniki/add_results.html',
        {
            'msg': name
        }
    )


def see_results(request, name, result_id):
    preview = Study.objects.get(study_id=result_id)
    result_date = str(preview.study_date)
    doctor_name = preview.doctor.doctor_name.replace(" ", "")
    if request.method == 'POST':
        preview.hospital = request.POST.get('hospital')
        preview.study_date = request.POST.get('date')
        preview.study_time = request.POST.get('time')
        preview.modality = request.POST.get('type')
        preview.note = request.POST.get('note')
        preview.filepath = request.POST.get('pathfile')
        preview.image = request.POST.get('image')

    else:
        msge = name
    return render(
        request,
        'wyniki/see_results.html',
        {
            'name': name,
            'msg': msge,
            'result': preview,
            'date': result_date,
            'doctor_name': doctor_name
        }
    )

def edit_results(request, name, result_id):
    edited_result = Study.objects.get(study_id=result_id)
    result_date = str(edited_result.study_date)

    if request.method == 'POST':
        if request.POST.get('patient_id') and request.POST.get('hospital') and request.POST.get(
                'date') and request.POST.get('type'):
            edited_result.hospital = request.POST.get('hospital')
            edited_result.study_date = request.POST.get('date')
            edited_result.study_time = request.POST.get('time')
            edited_result.modality = request.POST.get('type')
            edited_result.note = request.POST.get('note')
            edited_result.filepath = request.POST.get('pathfile')
            if len(request.FILES) != 0:
                edited_result.image = request.FILES['image']

            edited_result.save()
            msge = "Data updated to study table with id: " + str(edited_result.study_id)
            result_date = str(edited_result.study_date)
    else:
        msge = name
    return render(
        request,
        'wyniki/edit_results.html',
        {
            'name': name,
            'msg': msge,
            'result': edited_result,
            'date': result_date
        }
    )


def create_study(request, name):
    if request.method == 'POST':
        if request.POST.get('patient_id') and request.POST.get('hospital') and request.POST.get(
                'date') and request.POST.get('type'):
            one_study = Study()
            one_study.hospital = request.POST.get('hospital')
            one_study.study_date = request.POST.get('date')
            one_study.modality = request.POST.get('type')
            one_study.note = request.POST.get('note')
            one_study.pathfile = request.POST.get('pathfile')
            one_study.patient = Patient.objects.get(patient_id=request.POST.get('patient_id'))
            one_study.doctor = Doctor.objects.get(doctor_name=f'{request.user.first_name} {request.user.last_name}')
            
            if len(request.FILES) != 0:
                one_study.image = request.FILES['image']
            
            one_study.save()
            msge = "Data inserted to study table with id: " + str(one_study.study_id)
        else:
            msge = name
    else:
        msge = name

    return render(request, 'wyniki/add_results.html',
                  {
                      'msg': msge,
                  }
    )


# HOW TO DELETE - USEFUL COMMAND!!!
# Doctor.objects.filter(doctor_name="Gregory House").delete()
# https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models

def history(request, name):
    results_list = Study.objects.all()
    doctor_list = []
    doctor_results = []
    for r in results_list:
        doctor_name = r.doctor.doctor_name.replace(" ", "")
        doctor_list.append(doctor_name)
        if doctor_name == name:
            doctor_results.append(r)

    return render(
        request,
        'wyniki/history.html',
        {
            'results_list': results_list,
            'doctor_list': doctor_list,
            'doctor_results': doctor_results,
        }
    )


def create_patient(request):
    if request.method == 'POST':
        if request.POST.get('newUserName') and request.POST.get('firstname') and request.POST.get(
                'lastname') and request.POST.get('age') and request.POST.get('gender') and request.POST.get(
                'password1') and request.POST.get('password2') and request.POST.get('email'):
            
            if(request.POST.get('password1')==request.POST.get('password2')):
                new_user = User.objects.create(username=request.POST.get('newUserName'), email=request.POST.get('email'), password=request.POST.get('password2'))
                new_user.first_name = request.POST.get('firstname')
                new_user.last_name = request.POST.get('lastname')
                new_user.save()
                my_group = Group.objects.get(name='Pacjenci') 
                my_group.user_set.add(new_user)

            one_person = Patient()
            one_person.patient_name = request.POST.get('firstname') + ' ' + request.POST.get('lastname')
            one_person.age = request.POST.get('age')
            one_person.gender = request.POST.get('gender')            
            one_person.save()
            msge = "Registration successful. Data inserted to patient table with id: " + str(one_person.patient_id)
        else:
            msge = "Unsuccessful"
    else:
        msge = "Unsuccessful"

    return render(request, 'wyniki/home.html',
                  {
                      'msg': msge,
                  }
    )

def create_doctor(request):
    if request.method == 'POST':
        if request.POST.get('newUserName') and request.POST.get('firstname') and request.POST.get(
                'lastname') and request.POST.get('specialization') and request.POST.get(
                'password1') and request.POST.get('password2') and request.POST.get('email'):
            
            if(request.POST.get('password1')==request.POST.get('password2')):
                new_user = User.objects.create(username=request.POST.get('newUserName'), email=request.POST.get('email'), password=request.POST.get('password2'))
                new_user.first_name = request.POST.get('firstname')
                new_user.last_name = request.POST.get('lastname')
                new_user.save()
                my_group = Group.objects.get(name='Lekarze') 
                my_group.user_set.add(new_user)

            one_person = Doctor()
            one_person.doctor_name = request.POST.get('firstname') + ' ' + request.POST.get('lastname')
            one_person.specialization = request.POST.get('specialization')         
            one_person.save()
            msge = "Registration successful. Data inserted to doctor table with id: " + str(one_person.doctor_id)
        else:
            msge = "Unsuccessful"
    else:
        msge = "Unsuccessful"

    return render(request, 'wyniki/home.html',
                  {
                      'msg': msge,
                  }
    )
