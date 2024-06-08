from django.db.models import Avg
from django.shortcuts import render, redirect
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

def index_page(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    grades = Grade.objects.all()
    best_student = Grade.objects.values('student__first_name', 'student__last_name', 'student__patronymic').annotate(avg_grade=Avg('grade')).order_by('-avg_grade').first()
    worst_student = Grade.objects.values('student__first_name', 'student__last_name', 'student__patronymic').annotate(avg_grade=Avg('grade')).order_by('avg_grade').first()
    subject_avg_grades = Grade.objects.values('subject__name', 'subject__teacher').annotate(avg_grade=Avg('grade'))
    student_avg_grades = Grade.objects.values('student__first_name', 'student__last_name', 'student__patronymic').annotate(avg_grade=Avg('grade'))
    return render(request, 'index.html', {
        'students': students,
        'subjects': subjects,
        'grades': grades,
        'best_student': best_student,
        'worst_student': worst_student,
        'subject_avg_grades': subject_avg_grades,
        'student_avg_grades': student_avg_grades
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

def subject_avg_grades(request):
    subject_avg_grades = Grade.objects.values('subject__name', 'subject__teacher', 'student__first_name', 'student__last_name', 'student__patronymic', 'grade').annotate(avg_grade=Avg('grade'))
    return render(request, 'subject_avg_grades.html', {'subject_avg_grades': subject_avg_grades})

def student_avg_grades(request):
    student_avg_grades = Grade.objects.values('student__first_name', 'student__last_name', 'student__patronymic', 'subject__name', 'grade').annotate(avg_grade=Avg('grade'))
    return render(request, 'student_avg_grades.html', {'student_avg_grades': student_avg_grades})


