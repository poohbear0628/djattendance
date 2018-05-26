from rest_framework import serializers

from .models import Classnotes


class ClassnotesSerializer(serializers.ModelSerializer):
  status_display = serializers.CharField(source='get_status_display', read_only=True)

  class Meta:
    model = Classnotes
    fields = '__all__'
    read_only_fields = ['status', 'TA_comment', 'date_assigned', 'date_due',
      'date_submitted', 'content', 'submitting_paper_copy'
    ]
