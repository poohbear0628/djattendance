from django.contrib import admin

from terms.models import Term
from .models import AudioFile

admin.site.register(AudioFile)
