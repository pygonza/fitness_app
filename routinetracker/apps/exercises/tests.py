import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Exercise

User = get_user_model()

@pytest.mark.django_db
def test_exercise_creation():
    user = User.objects.create_user(username='test', password='secret123')
    exercise = Exercise.objects.create(
        name='Press de banca',
        muscle_group='push',
        type='strength',
        created_by=user,
    )
    assert exercise.created_by == user
    assert exercise.name == 'Press de banca'

@pytest.mark.django_db
def test_exercise_list_only_shows_owner(client):
    owner = User.objects.create_user(username='owner', password='secret123')
    other = User.objects.create_user(username='other', password='secret123')
    Exercise.objects.create(name='Sentadilla', muscle_group='legs', type='strength', created_by=owner)
    Exercise.objects.create(name='Remo', muscle_group='pull', type='strength', created_by=other)
    client.login(username='owner', password='secret123')
    response = client.get(reverse('exercises:list'))
    assert 'Sentadilla' in response.content.decode()
    assert 'Remo' not in response.content.decode()
