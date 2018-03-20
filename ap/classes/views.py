from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from aputils.decorators import group_required
from .forms import ClassFileForm
from .models import ClassFile


def upload(request):
  if request.method == 'POST':
    if request.user.has_group(['training_assistant']) or (request.POST.get('for_class') == 'Presentations'):
      form = ClassFileForm(request.POST, request.FILES, limit_choices=False)
      if form.is_valid():
        form.save()
    return redirect(reverse('classes:index'))


@group_required(['training_assistant'])
def delete_file(request, pk):
  ClassFile.objects.get(id=pk).delete()
  return redirect(reverse('classes:index'))


def class_files(request, classname=None):
  ctx = {
      'classname': classname,
  }

  if request.method == 'GET':
    if not classname and request.user.has_group(['training_assistant']):
      ctx['page_title'] = 'Class Files Administration'
      ctx['class_files'] = ClassFile.objects.all()
      ctx['form'] = ClassFileForm(limit_choices=False)
      ctx['delete'] = True
    else:
      classname = classname or 'Greek'
      if classname == 'Presentations':
        ctx['form'] = ClassFileForm(limit_choices=(('Presentations', 'Presentations'),))
      ctx['class_files'] = ClassFile.objects.filter(for_class=classname)
      ctx['page_title'] = '%s Files' % (classname)

  return render(request, 'classes/class_files.html', ctx)
