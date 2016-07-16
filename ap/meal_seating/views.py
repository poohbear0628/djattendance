  from django.shortcuts import render, redirect
  from django.views.decorators.csrf import csrf_protect
  from django.http import HttpResponse
  from meal_seating.models import Table, TraineeExclude
  from accounts.models import Trainee
  from datetime import date, timedelta
  from meal_seating.forms import TableFormSet, TraineeExcludeFormSet, TraineeExcludeForm


  @csrf_protect
  def editinfo(request):
    test = request.POST.getlist('to')
    print test
    isChecked = [int(x) for x in request.POST.getlist('to[]')]
    print set(isChecked)
    exclude_list = TraineeExclude.objects.values_list('trainee', flat=True)
    difference = set(exclude_list) - set(isChecked)
    addition = set(isChecked) - set(exclude_list)
    TraineeExclude.objects.all().filter(trainee__in=list(difference)).delete()
    aList = [TraineeExclude(trainee=val) for val in addition]
    TraineeExclude.objects.bulk_create(aList)
    
    return HttpResponse(difference)
  # try:
  #     obj = Person.objects.get(first_name='John', last_name='Lennon')
  # except Person.DoesNotExist:
  #     obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
  #     obj.save()

  def seattables(request):
      filterchoice = request.POST['Filter']
      genderchoice = request.POST['Gender']
      startdate = request.POST['startdate']
      enddate = request.POST['enddate']

      exclude_list = TraineeExclude.objects.values_list('trainee', flat=True)
      # trainees = User.objects.all().filter(is_active=1, gender=genderchoice).order_by(filterchoice)[:50]
      trainees = Trainee.objects.all().filter(is_active=1, gender=genderchoice).order_by(filterchoice)[:50]

      mydict = Table.seatinglist(trainees,genderchoice)

      return render(request, 'detail.html', {'mydict' : mydict, 'startdate':startdate, 'enddate': enddate})

  def newseats(request):
      form = TraineeExcludeForm()
      exclude_list = TraineeExclude.objects.values_list('trainee', flat=True)
      trainees_exclude = Trainee.objects.all().filter(pk__in=exclude_list)
      trainees = Trainee.objects.all().filter(is_active=1).order_by("lastname")
      tables = Table.objects.all()
      if request.method == 'POST':
      # we have multiple actions - save and delete in this case
        formset = TableFormSet(request.POST, queryset=Table.objects.all())

        print request.POST


        tables = Table.objects.all()

        ids = []

        # Table.objects.get()


          # iterate over all forms in the formset
        if formset.is_valid():
          formset.save(commit=False)
          print 'is valide'
          for form in formset.forms:

            print 'forms', form

            # help(form)

            # Only save form that's not empty and is valid
            if form.is_valid() and not (form.empty_permitted and not form.has_changed()):

              print 'form saving', form.empty_permitted, form.has_changed()
              # save + update

              m = form.save()

            # ids.append(m.id)

          # help(formset)

          print 'delet obx', formset.deleted_objects

          for obj in formset.deleted_objects:
            print 'delete', obj
            obj.delete()

        tables_delete = Table.objects.exclude(id__in=ids)

        # print 'delete', tables_delete, ids

        # tables_delete.delete()

        # redirect('newseating.html')

        formset = TableFormSet(queryset=Table.objects.all())

        return render(request, 'newseating.html', {'trainees' : trainees, 'tables':tables, 
      'formset':formset, 'trainees_exclude':trainees_exclude, 'form':form,})

      else:
        formset = TableFormSet(queryset=Table.objects.all())
        return render(request, 'newseating.html', {'trainees' : trainees, 'tables':tables, 
      'formset':formset, 'trainees_exclude':trainees_exclude,})

  def signin(request):
      trainees = Trainee.objects.all().filter(is_active=1).order_by("lastname")[:50]
      startdate = date.today()
      two_week_datelist = []
      for x in range(0,14):
          mydate = startdate + timedelta(days=x)
          two_week_datelist.append(format(mydate))
      return render(request, 'mealsignin.html', {'trainees' : trainees, 'start_date' : startdate, "two_week_datelist" : two_week_datelist})