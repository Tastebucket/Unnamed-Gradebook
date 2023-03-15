from django.shortcuts import render, redirect
from .models import Cohort, Assignment, Student, Grade
from .forms import GradeForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def cohorts_index(request):
  cohorts = Cohort.objects.all()
  return render(request, 'cohorts/index.html', {
    'cohorts': cohorts
  })

def cohorts_detail(request, cohort_id):
  cohort = Cohort.objects.get(id=cohort_id)
  students = Student.objects.filter(classes= cohort)
  grades = Grade.objects.all()
  grade_form = GradeForm()
  return render(request, 'cohorts/detail.html', {
    'cohort': cohort, 'students': students, 'grades':grades, 'grade_form':grade_form
    })

def add_score(request, grade_id, cohort_id):
  # Baby step
  form = GradeForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_grade = form.save(commit=False)
    new_grade.grade_id = grade_id
    new_grade.save()
  return redirect('detail', cohort_id=cohort_id)