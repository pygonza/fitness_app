from django.db import models


class WorkoutSession(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='workout_sessions')
    routine = models.ForeignKey('routines.Routine', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']
        unique_together = [['user', 'date']]

    @property
    def total_volume(self):
        return sum(set_entry.volume for set_entry in self.sets.all())

    def __str__(self):
        return f'Sesión {self.date} - {self.user.username}'


class WorkoutSet(models.Model):
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name='sets')
    exercise = models.ForeignKey('exercises.Exercise', on_delete=models.CASCADE)
    set_number = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.FloatField()
    completed = models.BooleanField(default=True)

    class Meta:
        ordering = ['exercise', 'set_number']

    @property
    def volume(self):
        return self.reps * self.weight

    def __str__(self):
        return f'{self.exercise.name} - Serie {self.set_number}'
