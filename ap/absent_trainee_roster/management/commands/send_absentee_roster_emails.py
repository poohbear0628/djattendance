from django.core.management.base import BaseCommand

from datetime import date, datetime
from django.core.mail import send_mail, mail_admins
from absent_trainee_roster.utils import send_absentee_report
from terms.models import Term

class Command(BaseCommand):
  # to use: python ap/manage.py send_absentee_roster_emails --settings=ap.settings.prod
  def _send_emails(self):
    # Only send email during the term
    today = date.today()
    if Term.current_term().is_date_within_term(today):
      send_absentee_report(today.year, today.month, today.day)
      print('Cron job emails sent!')
    else:
      print('Absentee report not sent because term not currently in session')


  def handle(self, *args, **options):
    self._send_emails()
