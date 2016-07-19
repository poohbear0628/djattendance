from datetime import date, datetime
from django.core.mail import send_mail, mail_admins
from absent_trainee_roster.utils import send_absentee_report
from terms.models import Term

# Only send email during the term
today = date.today()
if Term.current_term().is_date_within_term(today):
  send_absentee_report(today.year, today.month, today.day)
  print 'Cron job emails sent!'
else:
  print 'Absentee report not sent because term not currently in session'