from django.db import models

from terms.models import Term
from .utils import av_dir

class AVFile(models.Model):
  term = models.ForeignKey(Term)
