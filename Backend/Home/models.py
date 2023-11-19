from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class person_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    rollNumber = models.CharField(max_length=255)
    #courses_list = models.ManyToManyField(course_table)
    #course_list_created = models.ManyToManyField(course_table)


class course_table(models.Model):
    name = models.CharField(max_length=50)
    verification_code = models.TextField()
    teacher = models.ForeignKey(person_table, on_delete=models.CASCADE, related_name='teacher')
    students_list = models.ManyToManyField(person_table, related_name='students')


class session_record_table(models.Model):
    course_name = models.ForeignKey(course_table, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.TextField()


class attendance_record_table(models.Model):
    student_Id = models.ForeignKey(person_table, on_delete=models.CASCADE)
    session = models.ForeignKey(session_record_table, on_delete=models.CASCADE)
