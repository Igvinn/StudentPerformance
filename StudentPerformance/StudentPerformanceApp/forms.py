from django import forms
from .models import Student, Subject, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'patronymic')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        patronymic = cleaned_data.get('patronymic')

        if self.instance.pk is None:  # если это новый объект
            if Student.objects.filter(first_name=first_name, last_name=last_name, patronymic=patronymic).exists():
                raise forms.ValidationError("Student with this First Name, Last Name and Patronymic already exists.")
        return cleaned_data

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'teacher', 'hours')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        teacher = cleaned_data.get('teacher')

        if self.instance.pk is None:  # если это новый объект
            if Subject.objects.filter(name=name, teacher=teacher).exists():
                raise forms.ValidationError("Subject with this Name and Teacher already exists.")
        return cleaned_data

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('student', 'subject', 'grade')

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        subject = cleaned_data.get('subject')

        if self.instance.pk is None:  # если это новый объект
            if Grade.objects.filter(student=student, subject=subject).exists():
                raise forms.ValidationError("Grade for this Student and Subject already exists.")
        return cleaned_data
