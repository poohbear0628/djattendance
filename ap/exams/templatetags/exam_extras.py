from django import template

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

register.filter('lookup', lookup)
register.filter('score_display', score_display)
