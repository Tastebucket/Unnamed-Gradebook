from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cohorts/', views.cohorts_index, name= 'index'),
    path('cohorts/create/', views.CohortCreate.as_view(), name='cohorts_create'),
    path('cohorts/<int:cohort_id>/', views.cohorts_detail, name='detail'),
    path('cohorts/<int:pk>/update/', views.CohortUpdate.as_view(), name='cohorts_update'),
    path('cohorts/<int:pk>/delete/', views.CohortDelete.as_view(), name='cohorts_delete'),
    path('cohorts/<int:cohort_id>/add_score/<int:assignment_id>/<int:student_id>/', views.add_score, name='add_score'),
    path('cohorts/<int:cohort_id>/assign_form/', views.assign_form, name='assign_form'),
    path('cohorts/<int:cohort_id>/assign_form/add_assignment/', views.add_assignment, name='add_assignment'),
    path('cohorts/<int:cohort_id>/assoc_student/<int:student_id>/', views.assoc_student, name='assoc_student'),
    path('assignments/create/', views.AssignmentCreate.as_view(), name='assignments_create'),
    path('assignments/<int:pk>/update/', views.AssignmentUpdate.as_view(), name='assignments_update'),
    path('assignments/<int:pk>/delete/', views.AssignmentDelete.as_view(), name='assignments_delete'),
    path('assignments/<int:pk>/', views.AssignmentDetail.as_view(), name='assignments_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
