from datetime import *

import django_filters
from accounts.models import Trainee
from django.db.models import Q
from leaveslips.models import IndividualSlip
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

  def create(self, validated_data):
    trainee = validated_data['trainee']
    event = validated_data['event']
    date = validated_data['date']
    submitted_by = validated_data['submitted_by']
    status = validated_data['status']
    print validated_data

    # checks if roll exists for given trainee, event, and date
    roll_override = Roll.objects.filter(trainee=trainee, event=event.id, date=date)
    leaveslips = IndividualSlip.objects.filter(rolls=roll_override)
    SELF_ATTENDANCE_ROLL = trainee == submitted_by

    if roll_override.count() == 0 and status != 'P':  # if no pre-existing rolls, create
      return Roll.objects.create(**validated_data)
    elif roll_override.count() == 1:  # if a roll already exists,
      print 'maybe an audit roll'
      roll = roll_override.first()

      # no changes if there's no status change
      if status == 'P' and not leaveslips.exists():  # if input roll is "P" and no leave slip, delete it
        if SELF_ATTENDANCE_ROLL:
          if roll.trainee == submitted_by:
            roll_override.delete()
            return validated_data
          else:
            return validated_data
        else:
          roll_override.delete()
          return validated_data

      if roll.trainee.self_attendance and not SELF_ATTENDANCE_ROLL:
        print 'audit roll'
        if (roll.trainee == roll.submitted_by):
          return Roll.objects.create(**validated_data)
          return validated_data
        else:
          roll_override.update(**validated_data)
          roll_override.update(last_modified=datetime.now())
          return validated_data
      elif roll.trainee.self_attendance and SELF_ATTENDANCE_ROLL:
        if (roll.trainee == roll.submitted_by):
          roll_override.update(**validated_data)
          roll_override.update(last_modified=datetime.now())
          return validated_data
        else:
          return Roll.objects.create(**validated_data)
          return validated_data
      elif not roll.trainee.self_attendance:
        validated_data['submitted_by'] = self.context['request'].user
        roll_override.update(**validated_data)
        return validated_data
      return validated_data

    elif roll_override.count() == 2:  # if duplicate rolls
      if trainee.self_attendance:
        if SELF_ATTENDANCE_ROLL:
          r = roll_override.filter(submitted_by=submitted_by).first()
        else:
          r = roll_override.filter(~Q(submitted_by=trainee)).first()
      else:
        # THIS SHOULD NEVER HAPPEN
        r = roll_override.filter(~Q(submitted_by=submitted_by)).first()

      if r and r.status != status:
        if status == 'P':
          r.delete()
        else:
          r.status = status
          r.last_modified = datetime.now()
          r.save()
      return validated_data
    else:
      return validated_data


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
