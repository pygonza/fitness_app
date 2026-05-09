import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='tester', password='secret123', email='test@example.com')
    assert user.username == 'tester'
    assert user.email == 'test@example.com'

@pytest.mark.django_db
def test_profile_view_requires_login(client):
    response = client.get(reverse('users:profile'))
    assert response.status_code == 302

@pytest.mark.django_db
def test_signup_view_creates_user(client):
    response = client.post(reverse('users:signup'), {
        'username': 'nuevo',
        'email': 'nuevo@example.com',
        'password1': 'secret1234',
        'password2': 'secret1234',
        'unit_preference': 'kg',
        'timezone': 'UTC',
    })
    assert response.status_code == 302
    assert User.objects.filter(username='nuevo').exists()
