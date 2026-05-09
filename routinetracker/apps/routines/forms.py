from django import forms

from .models import Routine, RoutineExercise


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class RoutineExerciseForm(forms.ModelForm):
    class Meta:
        model = RoutineExercise
        fields = ['exercise', 'order', 'sets', 'reps', 'target_weight']
