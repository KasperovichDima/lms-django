# from django.shortcuts import render
from students.models import Student


def gen_std(request):
    return Student.generate_students(request)
