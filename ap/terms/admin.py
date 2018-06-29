from django.contrib import admin
from terms.models import Term

class TermAdmin(admin.ModelAdmin):
  list_display = ('name', 'current')
  ordering = ['start']

admin.site.register(Term, TermAdmin)
