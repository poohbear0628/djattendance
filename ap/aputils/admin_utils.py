from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
  # Other stuff here
  def has_delete_permission(self, request, obj=None):
    return False


class AddNotAllowedModelAdmin(admin.ModelAdmin):
  # Other stuff here
  def has_add_permission(self, request):
    return False


class FilteredSelectMixin(object):
  # Defines classes you want substitute widgets in for (e.g. [('residents', Trainee), ])
  registered_filtered_select = None

  def _save_set(self, DBObj, obj, attr, cleaned_data):
    id_set = set()
    for data in cleaned_data:
      id_set.add(data.id)

    getattr(obj, attr).clear()
    setattr(obj, attr, DBObj.objects.filter(id__in=id_set))

  def save_model(self, request, obj, form, change):
    # save first to obtain id
    super(FilteredSelectMixin, self).save_model(request, obj, form, change)
    print('before save', obj)
    for attr, DBObj in self.registered_filtered_select:
      self._save_set(DBObj, obj, attr, form.cleaned_data[attr])
    # 1/0
    print('after save')

  def get_form(self, request, obj=None, **kwargs):
    if obj:
      for attr, DBObj in self.registered_filtered_select:
        self.form.base_fields[attr].initial = [o.pk for o in getattr(obj, attr).all()]
    else:
      for attr, DBObj in self.registered_filtered_select:
        self.form.base_fields[attr].initial = []

    return self.form
