from django.conf import settings

def av_dir():
  return settings.MEDIA_ROOT or settings.AV_FILES_DIR
