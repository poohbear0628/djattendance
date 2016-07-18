from datetime import date, timedelta

import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.template import loader, Context
from django.core.mail import EmailMessage
from django.conf import settings # to get admin email addresses
from django.http import HttpResponse
from cgi import escape

from .models import Roster, User

def generate_pdf(year, month, day):
  #Retrieve data or whatever you need
  d=date(int(year),int(month),int(day))
  roster = Roster.objects.get(date=d)

  entries = roster.entry_set.all().order_by('-absentee')

  bro_entries = get_gender_separated_entries(entries, 'B')
  sis_entries = get_gender_separated_entries(entries, 'S')
  bro_unreported_houses = roster.unreported_houses.filter(gender='B')
  sis_unreported_houses = roster.unreported_houses.filter(gender='S')

  days = calculate_days(d)
  unreported_list = list_unreported_houses(d)
  return render_to_pdf(
    'absent_trainee_roster/generate_roster.html',
    {
      'pagsize': 'letter',
      'roster': roster,
      'bro_entries': bro_entries,
      'sis_entries': sis_entries,
      'genders': User.GENDER,
      'bro_unreported_houses': bro_unreported_houses,
      'sis_unreported_houses': sis_unreported_houses,
      'days': days,
      'unreported_list': unreported_list,
    }
  )

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def get_gender_separated_entries(entries, gender):
  absentee_list = []
  for entry in entries:
    name_in_list = entry.absentee.name.split()
    if len(name_in_list )==2:
      user = User.objects.filter(firstname=name_in_list[0], lastname=name_in_list[1]).first()
      if user.gender==gender:
        absentee_list.append(entry)
  return absentee_list

#calculate how many days a trainee has been absent in the last 7 days
def calculate_days(date):
  days = {}
  for i in range(7):
    try:
      roster = Roster.objects.get(date=date)
      for entry in roster.entry_set.all():
        if str(entry.absentee) in days:
          days[str(entry.absentee)] += 1
        else:
          days[str(entry.absentee)] = 1
    except:
      pass

    date = date - timedelta(days=1)
  return days

#makes list of trainee houses that are unreported within the last 7 days
def list_unreported_houses(date):
  list = []
  for i in range(7):
    try:
      roster = Roster.objects.get(date=date)
      for house in roster.unreported_houses.all():
        if house not in list:
          list.append(house)
    except:
      pass

    date = date - timedelta(days=1)
  return list


#sends absent trainee roster to admins
def send_absentee_report(year, month, day):
  d=date(int(year),int(month),int(day))
  roster = Roster.objects.get(date=d)
  entries = roster.entry_set.all().order_by('-absentee')
  bro_unreported_houses = roster.unreported_houses.filter(gender='B')
  sis_unreported_houses = roster.unreported_houses.filter(gender='S')

  days = calculate_days(d)
  unreported_list = list_unreported_houses(d)

  subject = "Absent Trainee Roster for " +str(d)
  email_template = loader.get_template('absent_trainee_roster/generate_roster.html')
  context = Context({
      'pagsize': 'letter',
      'roster': roster,
      'entries': entries,
      'bro_unreported_houses': bro_unreported_houses,
      'sis_unreported_houses': sis_unreported_houses,
    'days': days,
      'unreported_list': unreported_list,

    })

  admin_emails = [v for k,v in settings.ADMINS]
  email =EmailMessage(subject, email_template.render(context), 'djattendanceproject@gmail.com', admin_emails)
  email.content_subtype ="html"
  #email.attach('roster.pdf', self.generate_pdf, 'application/pdf')
  email.send(fail_silently=False)

def test_send_absentee_report():
  from datetime import date
  t = date.today()
  send_absentee_report(t.year, t.month, t.day)
