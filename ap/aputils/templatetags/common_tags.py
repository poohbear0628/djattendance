from django import template
from aputils.trainee_utils import is_trainee, is_TA
from django.template import NodeList, Variable
from django.contrib.auth.models import Group

register = template.Library()

register.filter('is_trainee', is_trainee)

register.filter('is_TA', is_TA)


def model_verbose_name(model):
  return model._meta.verbose_name


register.filter('model_verbose_name', model_verbose_name)


@register.tag()
def ifusergroup(parser, token):
  """ Check to see if the currently logged in user belongs to a specific
  group. Requires the Django authentication contrib app and middleware.

  Usage: {% ifusergroup Admins %} ... {% endifusergroup %}, or
       {% ifusergroup Admins|Group1|"Group 2" %} ... {% endifusergroup %}, or
       {% ifusergroup Admins %} ... {% else %} ... {% endifusergroup %}

  """
  try:
    tag, group = token.split_contents()
  except ValueError:
    raise template.TemplateSyntaxError("Tag 'ifusergroup' requires 1 argument.")

  nodelist_true = parser.parse(('else', 'endifusergroup'))
  token = parser.next_token()

  if token.contents == 'else':
    nodelist_false = parser.parse(('endifusergroup',))
    parser.delete_first_token()
  else:
    nodelist_false = NodeList()

  return GroupCheckNode(group, nodelist_true, nodelist_false)


class GroupCheckNode(template.Node):
  def __init__(self, group, nodelist_true, nodelist_false):
    self.group = group
    self.nodelist_true = nodelist_true
    self.nodelist_false = nodelist_false

  def render(self, context):
    user = Variable('user').resolve(context)
    if not user.is_authenticated:
       return self.nodelist_false.render(context)

    for group in self.group.split("|"):
      group = group[1:-1] if group.startswith('"') and group.endswith('"') else group
      try:
        if Group.objects.get(name=group) in user.groups.all():
          return self.nodelist_true.render(context)
      except Group.DoesNotExist:
        pass

    return self.nodelist_false.render(context)
