from django.contrib import admin

from terms.models import Term
from .models import AudioFile, AudioRequest

admin.site.register(AudioFile)
admin.site.register(AudioRequest)
