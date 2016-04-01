from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter(name='lookup')
def lookup(d, key):
    return d[key]

@register.filter(name='score_display')
def score_display(response):
    if response.score == None:
        return ""
    else:
        return response.score

@register.filter(name='question_string', needs_autoescape=True)
def question_string(question, autoescape=True):
    question = json.loads(question)
    if question['type'] == "essay":
        return mark_safe(question['prompt'] + ' <b>(Points: ' + question['points'] + ')</b>')
    else:
        return "Invalid question type"

@register.filter(name='response_string')
def response_string(response):
    if response == '':
        return ""
    response = json.loads(response)
    return response['response']

@register.filter(name='score_string')
def score_string(response):
    if response == '':
        return ""
    response = json.loads(response)
    return response['score']

@register.filter(name='comment_string')
def comment_string(response):
    if response == '':
        return ""
    response = json.loads(response)
    return response['comment']

# The next three functions return true if the box in question should be
# visible based on the visibility matrix provided.
@register.filter(name='responses_visible')
def responses_visible(visible):
    return visible[0]

@register.filter(name='scores_visible')
def scores_visible(visible):
    return visible[1]

@register.filter(name='comments_visible')
def comments_visible(visible):
    return visible[2]    

# The next three functions return the string "disabled" if the box in question
# should be uneditable based on the permissions matrix provided.
@register.filter(name='response_disabled')
def response_disabled(permissions):
    if permissions[0]:
        return ""
    else:
        return "disabled"

@register.filter(name='score_disabled')
def score_disabled(permissions):
    if permissions[1]:
        return ""
    else:
        return "disabled"

@register.filter(name='comment_disabled')
def comment_disabled(permissions):
    if permissions[2]:
        return ""
    else:
        return "disabled"

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