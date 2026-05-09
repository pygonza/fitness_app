from django.urls import path

from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.WorkoutSessionListView.as_view(), name='list'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create/', views.WorkoutSessionCreateView.as_view(), name='create'),
    path('<int:pk>/', views.WorkoutSessionDetailView.as_view(), name='detail'),
]
