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

register.filter('lookup', lookup)
register.filter('score_display', score_display)
register.filter('responses_visible', responses_visible)
register.filter('scores_visible', scores_visible)
register.filter('comments_visible', comments_visible)
register.filter('response_disabled', response_disabled)
register.filter('score_disabled', score_disabled)
register.filter('comment_disabled', comment_disabled)