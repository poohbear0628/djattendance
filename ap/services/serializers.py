from datetime import datetime
from .models import Worker, ServiceSlot, Service, WeekSchedule, Assignment
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

class ServiceActiveSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta(object):
    model = Service
    list_serializer_class = BulkListSerializer
    fields = ['id', 'active']

class WorkerIDSerializer(BulkSerializerMixin, ModelSerializer):
  # fullname = serializers.CharField(read_only=True)
  class Meta(object):
    model = Worker
    list_serializer_class = BulkListSerializer
    fields = ['id', 'full_name']


class WorkerAssignmentSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = Assignment
        list_serializer_class = BulkListSerializer
        fields = ['id', 'workers','service_slot','service','week_schedule']


class AssignmentPinSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta(object):
    model = Assignment
    list_serializer_class = BulkListSerializer
    fields = ['id', 'pin']