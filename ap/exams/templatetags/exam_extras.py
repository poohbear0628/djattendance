from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter(name='lookup')
def lookup(d, key):
    return d[key]

##############  FILTERS FOR SINGLE_EXAM_GRADES.HTML ##############
@register.filter(name='link_text')
def link_text(exam):
    if exam.is_graded:
        return exam.grade
    return "Grade exam"


register.filter('lookup', lookup)
register.filter('score_display', score_display)
register.filter('question_string', question_string)
register.filter('responses_visible', responses_visible)
register.filter('scores_visible', scores_visible)
register.filter('comments_visible', comments_visible)
register.filter('response_disabled', response_disabled)
register.filter('score_disabled', score_disabled)
register.filter('comment_disabled', comment_disabled)
register.filter('link_text', link_text)