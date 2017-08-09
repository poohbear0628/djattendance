from datetime import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from terms.models import Term
from schedules.models import Event
from accounts.models import Trainee
from .utils import audio_dir

fs = FileSystemStorage(location=audio_dir())

class AudioFileManager(models.Manager):
  def filter_week(self, week):
    term = Term.current_term()
    return sorted(filter(lambda f: f.week == week and f.term == term, self.all()), key=lambda f: f.date)

  def filter_term(self, term):
    return sorted(filter(lambda f: f.term == term, self.all()), key=lambda f: f.date)

class AudioFile(models.Model):

  objects = AudioFileManager()

  # File name format is something like this: B1-01 2017-03-02 DSady.mp3
  audio_file = models.FileField(storage=fs)

  def __unicode__(self):
    return '<Audio File {0}>'.format(self.audio_file.name)

  @property
  def code(self):
    try:
      return self.audio_file.name.split('_')[0].split('-')[0]
    except:
      return ''

  @property
  def date(self):
    try:
      return datetime.strptime(self.audio_file.name.split('_')[1], '%Y-%m-%d').date()
    except Exception as e:
      return

  @cached_property
  def term(self):
    try:
      t = filter(lambda term: term.is_date_within_term(self.date), Term.objects.all())
      return t[0] if t else None
    except:
      return

  @cached_property
  def event(self):
    try:
      return Event.objects.get(av_code=self.code)
    except:
      return

  @property
  def week(self):
    try:
      return int(self.audio_file.name.split('_')[0].split('-')[1])
    except:
      return

  @property
  def speaker(self):
    try:
      return self.audio_file.name.split('_')[-1].split('.')[0]
    except:
      return ''

class AudioRequestManager(models.Manager):
  def filter_term(self, term):
    ids = map(lambda f: f.id, AudioFile.objects.filter_term(term))
    return self.filter(audio_requested__in=ids).distinct()

class AudioRequest(models.Model):

  objects = AudioRequestManager()

  AUDIO_STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('F', 'Fellowship'),
    ('D', 'Denied'),
  )
  status = models.CharField(max_length=1, choices=AUDIO_STATUS, default='P')
  date_requested = models.DateTimeField(auto_now_add=True)
  trainee_author = models.ForeignKey(Trainee, null=True)
  TA_comments = models.TextField(null=True, blank=True)
  trainee_comments = models.TextField()
  audio_requested = models.ManyToManyField(AudioFile, related_name='audio_requests')

  @staticmethod
  def get_button_template():
    return 'audio/ta_buttons.html'

  @staticmethod
  def get_ta_button_template():
    return 'audio/ta_buttons.html'

  @staticmethod
  def get_detail_template():
    return 'audio/ta_detail.html'

  def get_trainee_requester(self):
    return self.trainee_author

  def get_status(self):
    return self.get_status_display()

  def get_date_created(self):
    return self.date_requested

  def get_category(self):
    return ', '.join(map(lambda a: a.code + ' week ' + str(a.week), self.audio_requested.all()))
