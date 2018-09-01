from datetime import *

import django_filters
from accounts.models import Trainee
from leaveslips.serializers import (GroupSlipSerializer,
                                    IndividualSlipSerializer)
from rest_framework import filters
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

from .models import Roll, RollsFinalization


class RollSerializer(BulkSerializerMixin, ModelSerializer):

  class Meta(object):
    model = Roll
    list_serializer_class = BulkListSerializer
    fields = ['id', 'event', 'trainee', 'status', 'finalized', 'notes', 'last_modified', 'submitted_by', 'date']
    validators = [UniqueTogetherValidator(
        queryset=Roll.objects.all(),
        fields=('trainee', 'event', 'date', 'submitted_by', 'status'),
        message='Duplication error for key fields, same status')]

  def update(self, instance, validated_data):

    instance.status = validated_data['status']
    instance.submitted_by = validated_data['submitted_by']
    instance.last_modified = datetime.now()
    instance.save()
    if not instance.leaveslips.exists() and instance.status == 'P':
      instance.delete()

    return instance

class RollFilter(filters.FilterSet):
  timestamp__lt = django_filters.DateTimeFilter(name='timestamp', lookup_expr='lt')
  timestamp__gt = django_filters.DateTimeFilter(name='timestamp', lookup_expr='gt')
  finalized = django_filters.BooleanFilter()

  class Meta:
    model = Roll
    fields = ['id', 'status', 'finalized', 'notes', 'last_modified', 'event', 'trainee', 'submitted_by', 'date']


class AttendanceSerializer(BulkSerializerMixin, ModelSerializer):
  name = SerializerMethodField('get_trainee_name')
  individualslips = IndividualSlipSerializer(many=True,)
  groupslips = GroupSlipSerializer(many=True, source='groupslip')
  rolls = RollSerializer(many=True, source='current_rolls')

  class Meta(object):
    model = Trainee
    list_serializer_class = BulkListSerializer
    fields = ['name', 'individualslips', 'groupslips', 'rolls']

  def get_trainee_name(self, obj):
    return obj.__unicode__()


class RollsFinalizationSerializer(BulkSerializerMixin, ModelSerializer):

  class Meta(object):
    model = RollsFinalization
    list_serializer_class = BulkListSerializer
    fields = ['weeks']
