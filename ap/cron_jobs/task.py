from datetime import datetime
from django.core.mail import send_mail, mail_admins

import os

try:
  #This runs a database backup script 
  os.system('/home/ftta-ap/backup.sh')
  print 'Backup ran:', datetime.now()
except:
  #Send out an email if backup script fails 
  subject = 'Backup Failed: ' + str(datetime.now())
  mail_admins(subject, 'Failed to backup database.', fail_silently=False)
