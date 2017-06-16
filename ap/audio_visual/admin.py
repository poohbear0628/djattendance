from django.contrib import admin

from .models import AVFile
from terms.models import Term

class AVFileAdmin(admin.ModelAdmin):
  def get_form(self, request, obj=None, **kwargs):
    form = super(AVFileAdmin, self).get_form(request, obj, **kwargs)
    form.base_fields['term'].initial = Term.current_term()
    return form
admin.site.register(AVFile, AVFileAdmin)
