from django.contrib import admin
from django.urls import include, path

from routinetracker.apps.workouts.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('routinetracker.apps.users.urls', namespace='users')),
    path('exercises/', include('routinetracker.apps.exercises.urls', namespace='exercises')),
    path('routines/', include('routinetracker.apps.routines.urls', namespace='routines')),
    path('workouts/', include('routinetracker.apps.workouts.urls', namespace='workouts')),
    path('', DashboardView.as_view(), name='dashboard'),
]
