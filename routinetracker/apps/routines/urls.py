from django.urls import path

from . import views

app_name = 'routines'

urlpatterns = [
    path('', views.RoutineListView.as_view(), name='list'),
    path('create/', views.RoutineCreateView.as_view(), name='create'),
    path('<int:pk>/', views.RoutineDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.RoutineUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.RoutineDeleteView.as_view(), name='delete'),
    path('<int:routine_pk>/exercise/add/', views.RoutineExerciseCreateView.as_view(), name='exercise_add'),
    path('exercise/<int:pk>/edit/', views.RoutineExerciseUpdateView.as_view(), name='exercise_edit'),
    path('exercise/<int:pk>/delete/', views.RoutineExerciseDeleteView.as_view(), name='exercise_delete'),
]
