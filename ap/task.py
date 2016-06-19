from datetime import datetime
from django.core.mail import send_mail

import os

try:
  #This runs a database backup script 
  os.system('/home/ftta-ap/backup.sh')
  print 'Backup ran:', datetime.now()
except:
  #Send out an email if backup script fails 
  subject = 'Backup Failed: ' + str(datetime.now())
  send_mail(subject, 'Failed to backup database.', 'server@ftta.com',
    ['attendanceproj@gmail.com'], fail_silently=False)
