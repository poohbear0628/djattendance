from django.contrib import admin

from .models import Portion

def approve(modeladmin, request, queryset):
  queryset.update(approved=True)

class PortionAdmin(admin.ModelAdmin):
  list_display = ('title', 'submitted_by', 'timestamp', 'approved')
  actions = [approve]
  search_fields = ['title', 'text', 'ref']

admin.site.register(Portion, PortionAdmin)
