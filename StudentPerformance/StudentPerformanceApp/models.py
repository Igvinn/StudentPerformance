from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    patronymic = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

class Subject(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    teacher = models.CharField(max_length=100, blank=False, null=False)
    hours = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"