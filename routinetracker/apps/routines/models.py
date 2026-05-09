from django.db import models


class Routine(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='routines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', 'name']
        unique_together = [['name', 'created_by']]

    def __str__(self):
        return self.name


class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_exercises')
    exercise = models.ForeignKey('exercises.Exercise', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)
    sets = models.PositiveSmallIntegerField(default=3)
    reps = models.PositiveSmallIntegerField(default=10)
    target_weight = models.FloatField(default=0.0)

    class Meta:
        ordering = ['order']
        unique_together = [['routine', 'exercise']]

    def __str__(self):
        return f'{self.routine.name} - {self.exercise.name}'
