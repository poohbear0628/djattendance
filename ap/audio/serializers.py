from rest_framework.serializers import ModelSerializer
from rest_framework_bulk import (
    BulkSerializerMixin,
)

from .models import AudioRequest

class AudioRequestSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta:
    model = AudioRequest
    fields = [
        'status',
        'date_requested',
        'trainee_author',
        'TA_comments',
        'trainee_comments',
        'audio_requested',
    ]
