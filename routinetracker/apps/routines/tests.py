import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Routine

User = get_user_model()

@pytest.mark.django_db
def test_routine_creation():
    user = User.objects.create_user(username='rutina', password='secret123')
    routine = Routine.objects.create(name='Fuerza', created_by=user)
    assert routine.created_by == user
    assert routine.name == 'Fuerza'

@pytest.mark.django_db
def test_routine_access_control(client):
    user = User.objects.create_user(username='rutina2', password='secret123')
    other = User.objects.create_user(username='otro', password='secret123')
    Routine.objects.create(name='Cardio', created_by=other)
    client.login(username='rutina2', password='secret123')
    response = client.get(reverse('routines:list'))
    assert response.status_code == 200
    assert 'Cardio' not in response.content.decode()
