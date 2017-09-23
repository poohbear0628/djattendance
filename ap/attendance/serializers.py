import django_filters
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Roll
from rest_framework import serializers, filters
from accounts.models import Trainee, User
from schedules.models import Event
from leaveslips.models import IndividualSlip, GroupSlip
from leaveslips.serializers import IndividualSlipSerializer, GroupSlipSerializer
from schedules.serializers import EventSerializer, ScheduleSerializer
from aputils.trainee_utils import trainee_from_user
from datetime import datetime
from rest_framework_bulk import (
  BulkListSerializer,
  BulkSerializerMixin,
  ListBulkCreateUpdateDestroyAPIView,
)

from datetime import datetime

class RollSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta(object):
    model = Roll
    list_serializer_class = BulkListSerializer
    fields = ['id','event','trainee','status','finalized','notes','last_modified','submitted_by','date']
  def create(self, validated_data):
    trainee = validated_data['trainee']
    event = validated_data['event']
    date = validated_data['date']
    validated_data['last_modified'] = datetime.now()
    submitted_by = trainee_from_user(self.context['request'].user)
    validated_data['submitted_by'] = submitted_by
    status = validated_data['status']

    # checks if roll exists for given trainee, event, and date
    roll_override = Roll.objects.filter(trainee=trainee, event=event.id, date=date, submitted_by=submitted_by)
    leaveslips = IndividualSlip.objects.filter(rolls=roll_override)

    # roll exists, so update
    if roll_override.exists():
      if status == 'P' and not leaveslips.exists(): #if marked as present, delete the roll, except if a leaveslip for it is present
        roll_override.delete()
      else:
        roll_override.update(**validated_data)
      return validated_data
    else: # no roll but event exists, so create roll
      if status != 'P':
        return Roll.objects.create(**validated_data)
      else:
        return validated_data

class RollFilter(filters.FilterSet):
  timestamp__lt = django_filters.DateTimeFilter(name = 'timestamp', lookup_expr = 'lt')
  timestamp__gt = django_filters.DateTimeFilter(name = 'timestamp', lookup_expr = 'gt')
  finalized = django_filters.BooleanFilter()
  class Meta:
    model = Roll
    fields = ['id','status','finalized','notes','last_modified','event','trainee','submitted_by','date']

class AttendanceSerializer(BulkSerializerMixin, ModelSerializer):
  name = SerializerMethodField('get_trainee_name')
  individualslips = IndividualSlipSerializer(many=True,)
  groupslips = GroupSlipSerializer(many=True,)
  rolls = RollSerializer(many=True,)
  class Meta(object):
    model = Trainee
    list_serializer_class = BulkListSerializer
    fields = ['name','individualslips','groupslips','rolls']
  def get_trainee_name(self, obj):
    return obj.__unicode__()
