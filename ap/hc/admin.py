from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from .models import HCSurvey, HCRecommendation


#admin.site.register(HCSurvey)
admin.site.register(HCRecommendation)


class JSONEditorWidget(forms.Widget):

    template_name = 'hc/jsoneditor.html'

    def render(self, name, value, attrs=None):
        context = {
            'data': value,
            'name': name
        }

        return mark_safe(render_to_string(self.template_name, context))


class HCSurveyAdminForm(forms.ModelForm):

    class Meta:
        model = HCSurvey
        fields = '__all__'
        widgets = {
            'trainee_comments': JSONEditorWidget()
        }

    class Media:
        css = { 'all': ('css/jsoneditor.min.css',) }
        js = ('js/jsoneditor.min.js', )


class HCSurveyAdmin(admin.ModelAdmin):
    list_display = ['pk']
    model = HCSurvey
    form = HCSurveyAdminForm

admin.site.register(HCSurvey, HCSurveyAdmin)