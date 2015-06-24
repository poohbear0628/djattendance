from django import template

register = template.Library()


@register.filter(name='lookup')
def lookup(d, key):
    return d[key]

# returns the text string response
@register.filter(name='response')
def response(responses, question_id):
	for response in responses:
		if response.question_id == question_id:
			return response.body
	return ""

register.filter('lookup', lookup)
register.filter('response', response)
