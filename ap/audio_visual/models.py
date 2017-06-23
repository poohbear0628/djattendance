from django.db import models
from django.core.files.storage import FileSystemStorage

from terms.models import Term
from .utils import av_dir

fs = FileSystemStorage(location=av_dir())

class AVFile(models.Model):
  term = models.ForeignKey(Term)
  audio_file = models.FileField(storage=fs)
