from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cohorts/', views.cohorts_index, name= 'index'),
    path('cohorts/<int:cohort_id>/', views.cohorts_detail, name='detail'),
    path('cohorts/<int:cohort_id>/add_score/<int:assignment_id>/<int:student_id>/', views.add_score, name='add_score'),
]
