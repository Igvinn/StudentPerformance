from django.contrib import admin
from StudentPerformanceApp.models import Student
from StudentPerformanceApp.models import Subject
from StudentPerformanceApp.models import Grade

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)