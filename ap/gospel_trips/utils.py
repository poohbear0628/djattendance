from .models import GospelTrip
import json


def export_to_json():
  gt = GospelTrip.objects.first()
  form = {'name': gt.name}
  form['sections'] = []
  for section in gt.section_set.all():
    form['sections'].append({
        'name': section.name,
        '_order': section._order})

    form['sections'][-1]['instructions'] = []
    for instruction in section.instruction_set.all():
      print instruction
      form['sections'][-1]['instructions'].append({
          'name': instruction.name,
          'instruction': instruction.instruction,
          '_order': instruction._order})

    form['sections'][-1]['questions'] = []
    for question in section.question_set.all():
      form['sections'][-1]['questions'].append({
          'instruction': question.instruction,
          'answer_type': question.answer_type,
          '_order': question._order})
  with open('result.json', 'w') as fp:
    json.dump(form, fp)
  return form
