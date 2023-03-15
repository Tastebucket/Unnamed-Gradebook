from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cohort, Assignment, Student, Grade
from django.views.generic.detail import DetailView
from .forms import GradeForm, AssignmentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'home.html')

@login_required
def cohorts_index(request):
  cohorts = Cohort.objects.filter(user=request.user)
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

def assign_form(request, cohort_id):
  cohort =  Cohort.objects.get(id=cohort_id)
  assignment_form = AssignmentForm()
  return render(request, 'assignments/form.html', {'cohort':cohort, 'assignment_form':assignment_form})

def add_assignment(request, cohort_id):
  # Baby step
  form = AssignmentForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_assignment = form.save(commit=False)
    new_assignment.cohort_id = cohort_id
    new_assignment.save()
  return redirect('detail', cohort_id=cohort_id)

class CohortCreate(LoginRequiredMixin,CreateView):
  model = Cohort
  fields = '__all__'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cohort
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class CohortUpdate(LoginRequiredMixin,UpdateView):
  model = Cohort
  fields = ['term']

class CohortDelete(LoginRequiredMixin,DeleteView):
  model = Cohort
  success_url = '/cohorts'

class AssignmentCreate(LoginRequiredMixin,CreateView):
  model = Assignment
  fields = '__all__'


class AssignmentUpdate(LoginRequiredMixin,UpdateView):
  model = Assignment
  fields = '__all__'

class AssignmentDelete(LoginRequiredMixin,DeleteView):
  model = Assignment
  success_url = '/cohorts'

class AssignmentDetail(LoginRequiredMixin,DetailView):
    model = Assignment
    template_name = 'assignments/detail.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
