from datetime import datetime
from django.core.mail import send_mail, mail_admins

import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

try:
  #This runs a database backup script 
  backup_path = SITE_ROOT + '/backup.sh'
  os.system(backup_path)
  print 'Backup ran:', datetime.now()
except:
  #Send out an email if backup script fails 
  subject = 'Backup Failed: ' + str(datetime.now())
  mail_admins(subject, 'Failed to backup database.', fail_silently=False)
