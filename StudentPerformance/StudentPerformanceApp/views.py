from django.shortcuts import render, redirect
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

def index_page(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    grades = Grade.objects.all()
    return render(request, 'index.html', {
        'students': students,
        'subjects': subjects,
        'grades': grades
    })

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SubjectForm()
    return render(request, 'create_subject.html', {'form': form})

def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GradeForm()
    return render(request, 'create_grade.html', {'form': form})

def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def update_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'update_subject.html', {'form': form})

def update_grade(request, pk):
    grade = Grade.objects.get(pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'update_grade.html', {'form': form})

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('index')

def delete_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    subject.delete()
    return redirect('index')

def delete_grade(request, pk):
    grade = Grade.objects.get(pk=pk)
    grade.delete()
    return redirect('index')
