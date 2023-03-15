from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Cohort(models.Model):
    title = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.title}, {self.term}"
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cohort_id': self.id})

class Assignment(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=400)
    category = models.TextField(max_length=100)
    weight = models.IntegerField()
    duedate = models.DateField("due date")
    def __str__(self):
        return f"Name: {self.name}, Due: {self.duedate}"
    def get_absolute_url(self):
        return reverse('assignments_detail', kwargs={'pk': self.id})

class Student(models.Model):
    name = models.TextField(max_length=100)
    email = models.CharField(max_length=100)
    classes = models.ManyToManyField(Cohort)
    assignments = models.ManyToManyField(Assignment, through='Grade')
    def __str__(self):
        return f"{self.name}"
    
class Grade(models.Model):
    score = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"student: {self.student} assignment:{self.assignment.name}"