from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'unit_preference', 'timezone', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('unit_preference', 'timezone', 'is_staff', 'is_active')
