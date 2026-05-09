from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ExerciseForm
from .models import Exercise


class ExerciseOwnerTestMixin(UserPassesTestMixin):
    def test_func(self):
        exercise = self.get_object()
        return exercise.created_by == self.request.user


class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Exercise.objects.filter(created_by=self.request.user)


class ExerciseDetailView(LoginRequiredMixin, ExerciseOwnerTestMixin, DetailView):
    model = Exercise
    template_name = 'exercises/exercise_detail.html'


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/exercise_form.html'
    success_url = reverse_lazy('exercises:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ExerciseUpdateView(LoginRequiredMixin, ExerciseOwnerTestMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/exercise_form.html'
    success_url = reverse_lazy('exercises:list')


class ExerciseDeleteView(LoginRequiredMixin, ExerciseOwnerTestMixin, DeleteView):
    model = Exercise
    template_name = 'exercises/exercise_confirm_delete.html'
    success_url = reverse_lazy('exercises:list')
