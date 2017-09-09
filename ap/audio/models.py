from datetime import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from terms.models import Term
from classnotes.models import Classnotes
from schedules.models import Event
from accounts.models import Trainee
from aputils.decorators import for_all_methods
from .utils import audio_dir

fs = FileSystemStorage(location=audio_dir())

def order_audio_files(files):
  files = sorted(files, key=lambda f: f.event.name)
  return sorted(files, key=lambda f:f.date)

def order_decorator(filter_function):
  def ordered_filter(*args, **kwargs):
    filtered = filter_function(*args, **kwargs)
    return order_audio_files(filtered)
  return ordered_filter

@for_all_methods(order_decorator)
class AudioFileManager(models.Manager):
  def filter_week(self, week):
    term = Term.current_term()
    return filter(lambda f: f.week == week and f.term == term, self.all())

  def filter_term(self, term):
    return filter(lambda f: f.term == term, self.all())

  def get_file(self, event, date):
    return filter(lambda f: f.event == event and f.date == date, self.all())

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

  def get_full_name(self):
    return 'Week {0} {1} by {2}'.format(self.week, self.event.name, self.speaker)

  def request(self, trainee):
    return self.audio_requests.filter(trainee_author=trainee).first()

  def classnotes(self, trainee):
    return Classnotes.objects.filter(trainee=trainee, event=self.event, date=self.date).first()

  def has_leaveslip(self, trainee):
    has_leaveslip = False
    attendance_record = trainee.attendance_record
    excused_events = filter(lambda r: r['attendance'] == 'E', attendance_record)
    for record in excused_events:
      d = datetime.strptime(record['start'].split('T')[0], '%Y-%m-%d').date()
      if record['event'] == self.event and d == self.date:
        has_leaveslip = True
    return has_leaveslip

  def can_download(self, trainee):
    request = self.request
    return self.has_leaveslip(trainee) or (request and request == 'A')

  def get_absolute_url(self):
    return reverse('audio:audio-update', kwargs={'pk': self.id})

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
