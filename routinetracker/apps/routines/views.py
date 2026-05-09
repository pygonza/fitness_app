from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import RoutineExerciseForm, RoutineForm
from .models import Routine, RoutineExercise


class RoutineOwnerTestMixin(UserPassesTestMixin):
    def test_func(self):
        routine = self.get_object()
        return routine.created_by == self.request.user


class RoutineListView(LoginRequiredMixin, ListView):
    model = Routine
    template_name = 'routines/routine_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Routine.objects.filter(created_by=self.request.user)


class RoutineDetailView(LoginRequiredMixin, RoutineOwnerTestMixin, DetailView):
    model = Routine
    template_name = 'routines/routine_detail.html'


class RoutineCreateView(LoginRequiredMixin, CreateView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routines/routine_form.html'
    success_url = reverse_lazy('routines:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class RoutineUpdateView(LoginRequiredMixin, RoutineOwnerTestMixin, UpdateView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routines/routine_form.html'
    success_url = reverse_lazy('routines:list')


class RoutineDeleteView(LoginRequiredMixin, RoutineOwnerTestMixin, DeleteView):
    model = Routine
    template_name = 'routines/routine_confirm_delete.html'
    success_url = reverse_lazy('routines:list')


class RoutineExerciseCreateView(LoginRequiredMixin, CreateView):
    model = RoutineExercise
    form_class = RoutineExerciseForm
    template_name = 'routines/routine_exercise_form.html'

    def form_valid(self, form):
        routine = Routine.objects.get(pk=self.kwargs['routine_pk'], created_by=self.request.user)
        form.instance.routine = routine
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('routines:detail', kwargs={'pk': self.kwargs['routine_pk']})


class RoutineExerciseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RoutineExercise
    form_class = RoutineExerciseForm
    template_name = 'routines/routine_exercise_form.html'

    def test_func(self):
        return self.get_object().routine.created_by == self.request.user

    def get_success_url(self):
        return reverse_lazy('routines:detail', kwargs={'pk': self.object.routine.pk})


class RoutineExerciseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = RoutineExercise
    template_name = 'routines/routine_exercise_confirm_delete.html'

    def test_func(self):
        return self.get_object().routine.created_by == self.request.user

    def get_success_url(self):
        return reverse_lazy('routines:detail', kwargs={'pk': self.object.routine.pk})
