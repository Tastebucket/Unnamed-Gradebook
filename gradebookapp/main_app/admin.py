from django.contrib import admin

from .models import Cohort, Student, Assignment, Grade

# Register your models here.
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Grade)
