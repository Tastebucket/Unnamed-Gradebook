from django.forms import ModelForm
from .models import Grade, Assignment

class GradeForm(ModelForm):
  class Meta:
    model = Grade
    fields = ['score']

class AssignmentForm(ModelForm):
  class Meta:
    model = Assignment
    fields = '__all__'