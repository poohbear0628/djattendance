from django_select2.forms import Select2MultipleWidget
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from ap.forms import TraineeSelectForm, EventSelectForm

class TraineeSelect2MultipleInput(Select2MultipleWidget):
  def render(self, name, value, attrs=None):
    output = super(TraineeSelect2MultipleInput, self).render(name, value, attrs)
    button = '<button type="button" class="btn btn-default" data-toggle="modal" data-target="#trainee_select"><span class="hide-if-in-class">Add Trainee Group</span></button>'
    select_modal = render_to_string('popups/trainee_select_modal.html', {'trainee_select_form': TraineeSelectForm()})
    return output + mark_safe(button) + mark_safe(select_modal)

  class Media:
    js = (
        'js/trainee_select.js',
    )

class EventSelect2MultipleInput(Select2MultipleWidget):
  def render(self, name, value, attrs=None):
    output = super(EventSelect2MultipleInput, self).render(name, value, attrs)
    button = '<button type="button" class="btn btn-default" data-toggle="modal" data-target="#event_select"><span class="hide-if-in-class">Add Event Group</span></button>'
    select_modal = render_to_string('popups/event_select_modal.html', {'event_select_form': EventSelectForm()})
    return output + mark_safe(button) + mark_safe(select_modal)

  class Media:
    js = (
        'js/event_select.js',
    )