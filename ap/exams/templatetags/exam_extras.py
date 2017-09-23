from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.filter(name='question_count')
def question_count(exam):
  total = 0
  for section in exam.sections.all():
    total += section.question_count
  return total
