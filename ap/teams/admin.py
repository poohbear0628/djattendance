from django.contrib import admin
from teams.models import Team
from accounts.models import Trainee


class TeamAdmin(admin.ModelAdmin):
  list_display = ('name', 'trainees',)
  search_fields = ('name', 'trainees',)

  def trainees(self, obj):
    return ", ".join([t.full_name for t in Trainee.objects.filter(team=obj)])


admin.site.register(Team, TeamAdmin)
