from django.db import models
from django.core.files.storage import FileSystemStorage
from audiofield.fields import AudioField

from .utils import av_dir
from terms.models import Term

class AVFile(models.Model):
  fs = FileSystemStorage(location=av_dir())
  ALLOWED_TYPES = ['.mp3', '.wav', '.ogg']
  audio_file = AudioField(storage=fs, blank=True,
            ext_whitelist=ALLOWED_TYPES,
            help_text=("Allowed types - " + ', '.join(ALLOWED_TYPES)))
  term = models.ForeignKey(Term)
