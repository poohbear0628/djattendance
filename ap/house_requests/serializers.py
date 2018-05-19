from rest_framework.serializers import ModelSerializer
from .models import MaintenanceRequest, LinensRequest, FramingRequest
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)


class MaintenanceSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta:
    model = MaintenanceRequest
    list_serializer_class = BulkListSerializer
    fields = '__all__'
    datatables_always_serialize = ['id', 'status', 'trainee_author', 'date_requested']


class LinensSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta:
    model = LinensRequest
    list_serializer_class = BulkListSerializer
    fields = '__all__'
    datatables_always_serialize = ['id', 'status', 'trainee_author', 'date_requested']


class FramingSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta:
    model = FramingRequest
    list_serializer_class = BulkListSerializer
    fields = '__all__'
    datatables_always_serialize = ['id', 'status', 'trainee_author', 'date_requested']
