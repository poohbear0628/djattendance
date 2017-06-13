import os.path

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from audiofield.fields import AudioField

from .utils import av_dir

class AVRequest(models.Model):
  fs = FileSystemStorage(location=av_dir())
  ALLOWED_TYPES = ['.mp3', '.wav', '.ogg']
  audio_file = AudioField(storage=fs, blank=True,
                    ext_whitelist=ALLOWED_TYPES,
                    help_text=("Allowed types - " + ', '.join(ALLOWED_TYPES)))

  def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
      file_url = av_dir() + str(self.audio_file)
      player_string = '<ul class="playlist"><li style="width:250px;">\
      <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
      return player_string
  audio_file_player.allow_tags = True
  audio_file_player.short_description = 'Audio file player'
