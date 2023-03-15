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
]
