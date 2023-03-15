from django.db import models

# Create your models here.
class Cohort(models.Model):
    title = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Name: {self.title}, {self.term}"

class Assignment(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=400)
    category = models.TextField(max_length=100)
    weight = models.IntegerField()
    duedate = models.DateField("due date")
    def __str__(self):
        return f"Name: {self.name}, Due: {self.duedate}"

class Student(models.Model):
    name = models.TextField(max_length=100)
    email = models.CharField(max_length=100)
    classes = models.ManyToManyField(Cohort)
    assignments = models.ManyToManyField(Assignment, through='Grade')
    def __str__(self):
        return f"Name: {self.name}"
    
class Grade(models.Model):
    score = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)