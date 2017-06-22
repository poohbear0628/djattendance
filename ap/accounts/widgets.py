from django_select2.forms import Select2MultipleWidget

class TraineeSelect2MultipleInput(Select2MultipleWidget):
  def render(self, name, value, attrs=None, choices=()):
    output = super(TraineeSelect2MultipleInput, self).render(name, value, attrs, choices)
    return output

  class Media:
    js = (
      'js/trainee_select.js',
    )