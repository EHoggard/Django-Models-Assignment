from django.contrib import admin
from .models import Student, School, Department, Faculty, Certificate, Grade 

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Certificate)
admin.site.register(Grade)

