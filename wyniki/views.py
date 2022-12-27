from django.shortcuts import render, redirect
from django.utils.timezone import datetime
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


def edit_results(request, name, result_id):
    edited_result = Study.objects.get(study_id=result_id)
    result_date = str(edited_result.study_date)

    if request.method == 'POST':
        if request.POST.get('patient_id') and request.POST.get('hospital') and request.POST.get(
                'date') and request.POST.get('type'):
            edited_result.hospital = request.POST.get('hospital')
            edited_result.study_date = request.POST.get('date')
            edited_result.modality = request.POST.get('type')
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
            one_study.patient = Patient.objects.get(patient_id=request.POST.get('patient_id'))
            one_study.doctor = Doctor.objects.get(doctor_name='John Watson')  # to change
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
