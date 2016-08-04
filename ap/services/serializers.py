from .models import Worker, ServiceSlot
from rest_framework import serializers, filters
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

from rest_framework.serializers import ModelSerializer



class UpdateWorkerSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta(object):
    model = Worker
    list_serializer_class = BulkListSerializer
    fields = ['id', 'health', 'services_cap']

class ServiceSlotWorkloadSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta(object):
    model = ServiceSlot
    list_serializer_class = BulkListSerializer
    fields = ['id', 'workers_required']
