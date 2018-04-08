import django_filters
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Roll
from rest_framework import filters
from datetime import *
from accounts.models import Trainee
from leaveslips.models import IndividualSlip
from leaveslips.serializers import IndividualSlipSerializer, GroupSlipSerializer
from aputils.trainee_utils import trainee_from_user
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)


class RollSerializer(BulkSerializerMixin, ModelSerializer):

  class Meta(object):
    model = Roll
    list_serializer_class = BulkListSerializer
    fields = ['id', 'event', 'trainee', 'status', 'finalized', 'notes', 'last_modified', 'submitted_by', 'date']

  def create(self, validated_data):
    trainee = validated_data['trainee']
    event = validated_data['event']
    date = validated_data['date']
    submitted_by = trainee_from_user(self.context['request'].user)
    validated_data['submitted_by'] = submitted_by
    status = validated_data['status']

    # checks if roll exists for given trainee, event, and date
    roll_override = Roll.objects.filter(trainee=trainee, event=event.id, date=date)
    leaveslips = IndividualSlip.objects.filter(rolls=roll_override)

    if roll_override.count() == 0 and status != 'P':  # if roll does not exist
      return Roll.objects.create(**validated_data)
    elif roll_override.count() == 1:  # if one roll
      if status == 'P' and not leaveslips.exists():  # if present roll with no leave slip, delete it
        roll_override.delete()
      else:  # otherwise, update the roll
        roll_override.update(**validated_data)
        roll_override.update(submitted_by=self.context['request'].user, last_modified=datetime.now())
      return validated_data
    elif roll_override.count() > 1:  # if duplicate rolls
      for r in roll_override:
        if not r.trainee.self_attendance:  # only update non-self attendance rolls
          r.status = status
          r.submitted_by = self.context['request'].user
          r.last_modified = datetime.now()
          r.save()
          roll_override = roll_override.filter(status=r.status, submitted_by=r.submitted_by, last_modified=r.last_modified)
          return validated_data

    # roll exists, so update
    # if roll_override.exists():
    #   if status == 'P' and not leaveslips.exists():  # if marked as present, delete the roll, except if a leave slip for it is present
    #     roll_override.delete()
    #   else:
    #     roll_override.update(**validated_data)
    #   return validated_data
    # else:  # no roll but event exists, so create roll
    #   if status != 'P':
    #     return Roll.objects.create(**validated_data)
    #   else:
    #     return validated_data


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
  rolls = RollSerializer(many=True,)

  class Meta(object):
    model = Trainee
    list_serializer_class = BulkListSerializer
    fields = ['name', 'individualslips', 'groupslips', 'rolls']

  def get_trainee_name(self, obj):
    return obj.__unicode__()
