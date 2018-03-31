from django.contrib import admin

from aputils.admin_utils import FilteredSelectMixin
from accounts.models import Trainee

from .models import Team
from .forms import TeamAdminForm


class TeamAdmin(FilteredSelectMixin, admin.ModelAdmin):
  list_display = ('name', 'trainees',)
  list_filter = ('name',)
  form = TeamAdminForm
  registered_filtered_select = [('members', Trainee), ]

  def trainees(self, obj):
    return ", ".join([t.full_name for t in Trainee.objects.filter(team=obj)])


admin.site.register(Team, TeamAdmin)
