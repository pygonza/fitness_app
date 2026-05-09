from collections import defaultdict
from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Sum
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import WorkoutSessionForm, WorkoutSetForm
from .models import WorkoutSession, WorkoutSet


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sessions = WorkoutSession.objects.filter(user=self.request.user, is_completed=True).order_by('-date')[:5]
        context['recent_sessions'] = sessions
        context['last_session'] = sessions.first()
        context['streak'] = self.get_training_streak()
        context['volume_data'] = self.get_volume_data()
        return context

    def get_training_streak(self):
        sessions = WorkoutSession.objects.filter(user=self.request.user, is_completed=True).order_by('-date')
        streak = 0
        today = date.today()
        expected = today
        for session in sessions:
            if session.date == expected:
                streak += 1
                expected -= timedelta(days=1)
            elif session.date < expected:
                break
        return streak

    def get_volume_data(self):
        sets = WorkoutSet.objects.filter(session__user=self.request.user, session__is_completed=True)
        grouped = defaultdict(float)
        for workout_set in sets:
            grouped[workout_set.exercise.name] += workout_set.volume
        return [{'exercise': key, 'volume': value} for key, value in grouped.items()]


class WorkoutSessionListView(LoginRequiredMixin, ListView):
    model = WorkoutSession
    template_name = 'workouts/session_list.html'
    paginate_by = 10

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user)


class WorkoutSessionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = WorkoutSession
    template_name = 'workouts/session_detail.html'

    def test_func(self):
        return self.get_object().user == self.request.user


class WorkoutSessionCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    form_class = WorkoutSessionForm
    template_name = 'workouts/session_form.html'
    success_url = reverse_lazy('workouts:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
