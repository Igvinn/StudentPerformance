# Generated by Django 5.0.6 on 2024-06-05 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentPerformanceApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_grade',
        ),
    ]
