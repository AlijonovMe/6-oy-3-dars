from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('student/<int:pk>/', student, name='student'),
    path('course/<int:pk>/', course, name='course')
]