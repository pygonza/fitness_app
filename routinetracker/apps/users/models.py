from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    WEIGHT_UNITS = [
        ('kg', 'Kilogramos'),
        ('lb', 'Libras'),
    ]

    unit_preference = models.CharField(
        max_length=2,
        choices=WEIGHT_UNITS,
        default='kg',
        help_text='Unidad de peso preferida del usuario.',
    )
    timezone = models.CharField(
        max_length=50,
        default='UTC',
        help_text='Zona horaria preferida para el registro de sesiones.',
    )

    def __str__(self):
        return self.get_full_name() or self.username
