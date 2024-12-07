from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import *

def home(request: WSGIRequest):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students
    }
    return render(request, 'home.html', context)

