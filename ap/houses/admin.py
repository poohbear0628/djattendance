from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from accounts.models import Trainee
from houses.models import House, Room, Bunk
from aputils.models import Address


class HouseForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        label='Residents',
        queryset=Trainee.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            "trainees", is_stacked=False))

    class Meta:
        model = House
        fields = ['name', 'address', 'gender', 'used',]
        widgets = {
            'permissions': admin.widgets.FilteredSelectMultiple(
                "permissions", is_stacked=False),
        }


class HouseAdmin(ModelAdmin):
    form = HouseForm

    list_display = ['name', 'address', 'gender', 'used', 'residents_list', ]
    ordering = ['name',]

    def save_model(self, request, obj, form, change):
        # save first to obtain id
        super(HouseAdmin, self).save_model(request, obj, form, change)
        obj.residents.clear()
        for user in form.cleaned_data['users']:
             obj.residents.add(user)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form.base_fields['users'].initial = [o.pk for o in obj.residents.all()]
        else:
            self.form.base_fields['users'].initial = []
        return HouseForm


admin.site.register(House, HouseAdmin)
admin.site.register(Room)
admin.site.register(Bunk)
