from django.db import models

class ImportFile(models.Model):
    docfile = models.FileField(upload_to='csvfiles')
