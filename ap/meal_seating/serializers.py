from .models import Table
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_bulk import (
  BulkListSerializer,
  BulkSerializerMixin,
  ListBulkCreateUpdateDestroyAPIView,
)

class TableSerializer(ModelSerializer):
  class Meta:
    model = Table
    fields = '__all__'
