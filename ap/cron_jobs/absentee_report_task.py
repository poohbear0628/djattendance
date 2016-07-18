from datetime import date
from django.core.mail import send_mail, mail_admins
from absent_trainee_roster.utils import send_absentee_report

today = date.today()
send_absentee_report(today.year, today.month, today.day)