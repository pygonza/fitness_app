import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import WorkoutSession

User = get_user_model()

@pytest.mark.django_db
def test_workout_session_volume_property():
    user = User.objects.create_user(username='entreno', password='secret123')
    session = WorkoutSession.objects.create(user=user, date='2026-05-09', is_completed=True)
    assert session.total_volume == 0

@pytest.mark.django_db
def test_dashboard_requires_login(client):
    response = client.get(reverse('dashboard'))
    assert response.status_code == 302
