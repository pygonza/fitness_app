from django.contrib import admin

from .models import Routine, RoutineExercise


class RoutineExerciseInline(admin.TabularInline):
    model = RoutineExercise
    extra = 1


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'updated_at')
    search_fields = ('name', 'description')
    inlines = [RoutineExerciseInline]


@admin.register(RoutineExercise)
class RoutineExerciseAdmin(admin.ModelAdmin):
    list_display = ('routine', 'exercise', 'order', 'sets', 'reps', 'target_weight')
    list_filter = ('routine',)
