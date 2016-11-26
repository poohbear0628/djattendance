from .models import Table, TraineeExclusion
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from accounts.serializers import TraineeSerializer
from rest_framework_bulk import (
  BulkListSerializer,
  BulkSerializerMixin,
  ListBulkCreateUpdateDestroyAPIView,
)

class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class TraineeExclusionSerializer(ModelSerializer):
    class Meta:
        model = TraineeExclusion
        fields = '__all__'
