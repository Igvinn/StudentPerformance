from django import forms
from .models import Student, Subject, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'patronymic')

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'teacher', 'hours')

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('student', 'subject', 'grade')
