from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from aputils.decorators import group_required
from .forms import ClassFileForm
from .models import ClassFile


@group_required(['training_assistant'])
def upload(request):
  if request.method == 'POST':
    form = ClassFileForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect(reverse('classes:index'))


@group_required(['training_assistant'])
def delete_file(request, pk):
  ClassFile.objects.get(id=pk).delete()
  return redirect(reverse('classes:index'))


def class_files(request, classname=None):
  ctx = {}

  if request.method == 'GET':
    if classname is None:
      ctx['page_title'] = 'Class Files'
      if request.user.has_group(['training_assistant']):
        ctx['class_files'] = ClassFile.objects.all()
        ctx['form'] = ClassFileForm()
        ctx['delete'] = True
    else:
      ctx['class_files'] = ClassFile.objects.filter(for_class=classname)
      ctx['page_title'] = '%s Files' % (classname)

  return render(request, 'classes/class_files.html', ctx)
