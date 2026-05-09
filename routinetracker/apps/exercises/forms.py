from django import forms

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_group', 'type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
