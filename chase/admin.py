from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_lives', 'tabs_switched')
    search_fields = ('name',)