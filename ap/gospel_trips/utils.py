import json
import os

from django.conf import settings  # for access to MEDIA_ROOT
from datetime import datetime
from .models import GospelTrip, Instruction, Question, Section

JSON_FILE_DIR = os.path.join('gospel_trips', 'exports')


def export_to_json(pk):
  try:
    gt = GospelTrip.objects.get(pk=pk)
  except GospelTrip.DoesNotExist:
    return ''

  file_path = os.path.join(settings.MEDIA_ROOT, JSON_FILE_DIR)
  full_path = os.path.join(file_path, gt.name.replace(' ', '_') + '.json')
  dir = os.path.dirname(full_path)
  if not os.path.isdir(dir):
    os.makedirs(dir)

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
  j = json.dumps(form, indent=2)
  f = open(full_path, 'w')
  print >> f, j  # TODO: Python3
  f.close()
  return full_path


def json_to_python(path):
  '''this function does not validate. Please use export_to_json. '''
  f = open(path)
  data = json.load(f)
  try:
    gt = GospelTrip(name=data['name'] + ' (Copy)', open_time=datetime(2018, 1, 1), close_time=datetime(2018, 1, 1))
    gt.save()
    for section in data['sections']:
      sec = Section(_order=section['_order'], name=section['name'], gospel_trip=gt)
      sec.save()
      for instruction in section['instructions']:
        inst = Instruction(_order=instruction['_order'], name=instruction['name'], section=sec)
        inst.save()
      for question in section['questions']:
        quest = Question(_order=question['_order'], instruction=question['instruction'], answer_type=question['answer_type'], section=sec)
        quest.save()
    return 1
  except AttributeError:
    return 0
