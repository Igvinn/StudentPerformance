from django.shortcuts import render
from .models import Student, Subject, Grade

def index_page(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    grades = Grade.objects.all()
    return render(request, 'index.html', {
        'students': students,
        'subjects': subjects,
        'grades': grades
    })
