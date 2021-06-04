from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Department(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    DEPT_name = models.CharField(max_length=400)
    full_name = models.CharField(max_length=40)

    def __str__(self):
        return self.DEPT_name

class Certificate(models.Model):
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Grade(models.Model):
    letter = models.CharField(max_length=2)

    def __str__(self):
        return self.letter

class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    Certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40)
    YOG = models.IntegerField()
    date_of_resumption = models.DateField(default=datetime.today)

    def __str__(self):
        return self.full_name

class Faculty(models.Model):
    name = models.ForeignKey(Department, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40)


    def __str__(self):
        return self.full_name

