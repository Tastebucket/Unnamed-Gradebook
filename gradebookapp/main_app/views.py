from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  student_ids = Student.objects.filter(classes= cohort).values_list('id', flat=True)
  grades = Grade.objects.all()
  grade_ids =Grade.objects.all().values_list('assignment', flat=True)
  grade_studs =Grade.objects.all().values_list('student', flat=True)
  grade_tuples=[]
  for i in range(len(grades)):
    grade_tuples.append((grade_ids[i], grade_studs[i]))
  grade_form = GradeForm()
  assignment_ids = Assignment.objects.filter(cohort= cohort).values_list('id', flat=True)
  other_tuples=[]
  for i in range(len(students)):
    for j in range(len(assignment_ids)):
      other_tuples.append((assignment_ids[j], student_ids[i]))
  new_tuples=[]
  for i in range(len(other_tuples)):
    if other_tuples[i] not in grade_tuples:
      new_tuples.append(other_tuples[i])
  return render(request, 'cohorts/detail.html', {
    'cohort': cohort, 'students': students, 'grades':grades, 'grade_form':grade_form, 'new_tuples':new_tuples
    })

def add_score(request, assignment_id, student_id, cohort_id):
  # Baby step
  form = GradeForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_grade = form.save(commit=False)
    new_grade.assignment_id = assignment_id
    new_grade.student_id = student_id
    new_grade.save()
  return redirect('detail', cohort_id=cohort_id)

class CohortCreate(CreateView):
  model = Cohort
  fields = '__all__'

class CohortUpdate(UpdateView):
  model = Cohort
  fields = ['term']

class CohortDelete(DeleteView):
  model = Cohort
  success_url = '/cohorts'