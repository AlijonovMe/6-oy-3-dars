from django.shortcuts import render, get_object_or_404
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

def course(request: WSGIRequest, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.filter(course=course)
    context = {
        'course': course,
        'students': students
    }

    return render(request, 'courses.html', context)

def student(request: WSGIRequest, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student
    }
    return render(request, 'students.html', context)

