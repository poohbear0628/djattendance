from datetime import date, timedelta

from django.contrib import admin
from django.template import loader,Context
from django.conf.urls import url
from django.core.mail import EmailMessage
from django.conf import settings # to get admin email addresses
from django.http import HttpResponse

from .models import Absentee, Roster, Entry
from .utils import *
from .views import email, email_on_date, pdf_report

from houses.models import House
from accounts.models import User

class EntryAdmin(admin.ModelAdmin):
  ordering = ('-roster__date',)

  def house(obj):
    return obj.absentee.house

  def term(obj):
    return obj.absentee.term

  list_display = ('roster', 'absentee', 'reason', 'comments', house,)


class EntryInline(admin.TabularInline):
  model = Entry
  fk_name = 'roster'
  verbose_name_plural = 'entries'
  extra = 1


class RosterAdmin(admin.ModelAdmin):

  ordering = ('-date',)

  def unreported_houses_count(obj):
    return obj.unreported_houses.all().count()

  def absentee_count(obj):
    return obj.entry_set.all().count()

  list_display = ('date', unreported_houses_count, absentee_count, 'notes', )

  inlines = [
    EntryInline,
  ]

  readonly_fields = ('unreported_houses',)

  def save_related(self, request, form, formsets, change):
    roster = Roster.objects.get(date=request.POST['date'])

    # when roster is created, add all houses as unreported.
    # --this is also done in RosterManager.create_roster(), but
    # admin doesn't call this function to create objects.
    if not change:
      for house in House.objects.all():
        roster.unreported_houses.add(house)
        roster.save()

    for formset in formsets:
      self.save_formset(request, form, formset, change)

    return True

  def save_formset(self, request, form, formset, change):
    roster = Roster.objects.get(date=request.POST['date'])
    entries = formset.save(commit=False)
    for entry in entries:
      roster.unreported_houses.remove(entry.absentee.house)
      entry.save()
    formset.save_m2m()
    return True

  def get_urls(self):
    urls = super(RosterAdmin, self).get_urls()
    my_urls = [
      url(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d+)/change/generate/$', self.admin_site.admin_view(self.generate_pdf)),
      url(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d+)/change/email/$', self.admin_site.admin_view(self.send_mail)),
    ]
    return my_urls +urls

  #using Pisa
  def generate_pdf(self, request, year, month, day):
    return generate_pdf(year, month, day)

  #sends absent trainee roster to admins
  def send_mail(self,request, year, month, day):
    send_absentee_report(year, month, day)
    return HttpResponse("Email was sent for %s-%s-%s" % (month, day, year))

# admin.site.register(Absentee)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Entry, EntryAdmin)
