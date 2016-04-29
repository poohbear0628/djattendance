import django_filters
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Roll, Event
from rest_framework import serializers, filters
from accounts.models import Trainee
from leaveslips.models import IndividualSlip, GroupSlip
from leaveslips.serializers import IndividualSlipSerializer, GroupSlipSerializer
from schedules.serializers import EventSerializer, ScheduleSerializer
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

class RollSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = Roll
        list_serializer_class = BulkListSerializer
        fields = ['id','event','trainee','status','finalized','notes','timestamp','monitor','date']
    def create(self, validated_data):
    	data_trainee = validated_data['trainee']
    	data_event = validated_data['event']
        data_date = validated_data['date']
    	# checks if roll exists for given trainee, event, and date
    	roll_override = Roll.objects.filter(trainee=data_trainee).filter(event=data_event.id).filter(date=data_date)
    	# checks if event exists for given event and date
    	event_override = Event.objects.filter(name=data_event.name).filter(weekday=data_date.weekday())
        
        if not event_override: # no event, then don't do anything
        	return validated_data
        elif not roll_override: # no roll, then create roll
        	return Roll.objects.create(**validated_data)
        else: # else there is a roll and there is an event, so update
            roll_override.update(**validated_data)
            return validated_data

class RollFilter(filters.FilterSet):
    timestamp__lt = django_filters.DateTimeFilter(name = 'timestamp', lookup_expr = 'lt')
    timestamp__gt = django_filters.DateTimeFilter(name = 'timestamp', lookup_expr = 'gt')
    finalized = django_filters.BooleanFilter()
    class Meta:
        model = Roll
        fields = ['id','status','finalized','notes','timestamp','event','trainee','monitor','date']

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

class AttendanceFilter(filters.FilterSet):
	class Meta:
		model = Trainee
		fields = ['id','individualslips','groupslips','rolls','term']