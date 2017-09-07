from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter(name='lookup')
def lookup(d, key):
  return d[key]


@register.filter(name='is_taking_exam')
def is_taking_exam(role):
  return role in ("Take")


@register.filter(name='link_text')
def link_text(exam):
  if exam.is_graded:
    return exam.grade
  return "Grade exam"


@register.filter(name='question_count')
def question_count(exam):
  total = 0
  for section in exam.sections.all():
    total += section.question_count
  return total

register.filter('lookup', lookup)
register.filter('is_taking_exam', is_taking_exam)
register.filter('link_text', link_text)
register.filter('question_count', question_count)