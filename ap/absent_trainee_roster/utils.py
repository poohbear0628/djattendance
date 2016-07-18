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

from collections import Counter


def build_report_ctx(date):
  roster = Roster.objects.get(date=date)
  entries = roster.entry_set.all().order_by('-absentee')

  bro_entries = roster.entry_set.filter(absentee__gender='B').order_by('absentee__firstname', 'absentee__lastname')
  sis_entries = roster.entry_set.filter(absentee__gender='S').order_by('absentee__firstname', 'absentee__lastname')
  bro_unreported_houses = roster.unreported_houses.filter(gender='B')
  sis_unreported_houses = roster.unreported_houses.filter(gender='S')

  trainee_absent_freq = calculate_trainee_absent_freq(date)
  unreported_list = list_unreported_houses(date)

  return {
    'pagsize': 'letter',
    'roster': roster,
    'bro_entries': bro_entries,
    'sis_entries': sis_entries,
    'genders': User.GENDER,
    'bro_unreported_houses': bro_unreported_houses,
    'sis_unreported_houses': sis_unreported_houses,
    'trainee_absent_freq': trainee_absent_freq,
    'unreported_list': unreported_list,
  }

def generate_pdf(year, month, day):
  #Retrieve data or whatever you need
  d = date(int(year),int(month),int(day))
  ctx = build_report_ctx(d)

  return render_to_pdf(
    'absent_trainee_roster/generate_roster.html',
    ctx
  )

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


#calculate how many days a trainee has been absent in the last 7 days
# Returns: {trainee.id: absent_count,}
def calculate_trainee_absent_freq(date):
  absent_tb = Counter()
  for i in range(7):
    if Roster.objects.filter(date=date).count() == 1:
      roster = Roster.objects.get(date=date)
      for entry in roster.entry_set.all():
        absent_tb[entry.absentee.id] += 1

    date = date - timedelta(days=1)
  return absent_tb

#makes list of trainee houses that are unreported within the last 7 days
def list_unreported_houses(date):
  list = []
  for i in range(7):
    if Roster.objects.filter(date=date).count() == 1:
      roster = Roster.objects.get(date=date)
      for house in roster.unreported_houses.all():
        if house not in list:
          list.append(house)

    date = date - timedelta(days=1)
  return list


#sends absent trainee roster to admins
def send_absentee_report(year, month, day):
  d = date(int(year),int(month),int(day))
  ctx = build_report_ctx(d)

  subject = "Absent Trainee Roster for " + str(d)
  email_template = loader.get_template('absent_trainee_roster/generate_roster.html')
  context = Context(ctx)

  recipients_emails = settings.ABSENTEE_ROSTER_RECIPIENTS
  email = EmailMessage(subject, email_template.render(context), 'djattendanceproject@gmail.com', recipients_emails)
  email.content_subtype ="html"
  pdf_data = generate_pdf(year, month, day)
  email.attach('roster.pdf', pdf_data.content, 'application/pdf')
  email.send(fail_silently=False)

def test_send_absentee_report():
  from datetime import date
  t = date.today()
  send_absentee_report(t.year, t.month, t.day)
