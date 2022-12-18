import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django import template


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
            'name': name,
        }
    )


def is_member(user):
    return user.groups.filter(name='Lekarze').exists()

