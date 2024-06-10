from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# models.py
from django.db.models import UniqueConstraint

class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    patronymic = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['first_name', 'last_name', 'patronymic'], name='unique_student')
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

class Subject(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    teacher = models.CharField(max_length=100, blank=False, null=False)
    hours = models.IntegerField(default=1, blank=False, null=False, validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['name', 'teacher'], name='unique_subject')
        ]

    def __str__(self):
        return f"{self.name} ({self.teacher})"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(2, message="Grade must be at least 2"),
            MaxValueValidator(5, message="Grade cannot exceed 5")
        ]
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['student', 'subject'], name='unique_student_subject')
        ]

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"
