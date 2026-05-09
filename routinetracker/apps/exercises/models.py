from django.db import models


class Exercise(models.Model):
    MUSCLE_GROUP_CHOICES = [
        ('push', 'Empuje'),
        ('pull', 'Jalón'),
        ('legs', 'Pierna'),
        ('core', 'Core'),
        ('cardio', 'Cardio'),
    ]

    EXERCISE_TYPE_CHOICES = [
        ('strength', 'Pesas'),
        ('cardio', 'Cardio'),
        ('mobility', 'Movilidad'),
        ('bodyweight', 'Peso corporal'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    muscle_group = models.CharField(max_length=20, choices=MUSCLE_GROUP_CHOICES)
    type = models.CharField(max_length=20, choices=EXERCISE_TYPE_CHOICES)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='exercises')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        unique_together = [['name', 'created_by']]

    def __str__(self):
        return self.name
