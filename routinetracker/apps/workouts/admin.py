from django.contrib import admin

from .models import WorkoutSession, WorkoutSet


class WorkoutSetInline(admin.TabularInline):
    model = WorkoutSet
    extra = 1


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'date')
    search_fields = ('notes',)
    inlines = [WorkoutSetInline]


@admin.register(WorkoutSet)
class WorkoutSetAdmin(admin.ModelAdmin):
    list_display = ('session', 'exercise', 'set_number', 'reps', 'weight', 'completed')
    list_filter = ('completed',)
