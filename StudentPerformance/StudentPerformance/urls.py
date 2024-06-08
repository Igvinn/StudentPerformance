"""
URL configuration for StudentPerformance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from StudentPerformanceApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_subject/', views.create_subject, name='create_subject'),
    path('create_grade/', views.create_grade, name='create_grade'),
    path('update_student/<pk>/', views.update_student, name='update_student'),
    path('update_subject/<pk>/', views.update_subject, name='update_subject'),
    path('update_grade/<pk>/', views.update_grade, name='update_grade'),
    path('delete_student/<pk>/', views.delete_student, name='delete_student'),
    path('delete_subject/<pk>/', views.delete_subject, name='delete_subject'),
    path('delete_grade/<pk>/', views.delete_grade, name='delete_grade'),
]