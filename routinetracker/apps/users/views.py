from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from .forms import UserRegisterForm, UserProfileForm
from .models import User


class SignUpView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Bienvenido a RoutineTracker. Tu cuenta fue creada exitosamente.')
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Tus datos se actualizaron correctamente.')
        return super().form_valid(form)
