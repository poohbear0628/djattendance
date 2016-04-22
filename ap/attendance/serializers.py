import django_filters
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Roll
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
        fields = '__all__'
    def create(self, validated_data):
    	data_id = validated_data['event'].id
    	data_timestart = validated_data['timestart']
    	override = Roll.objects.filter(event=data_id).filter(timestart=data_timestart)
    	if not override:
    		return Roll.objects.create(**validated_data)
    	else:
    		return override.update(**validated_data)

class RollFilter(filters.FilterSet):
    timestamp__lt = django_filters.DateTimeFilter(name = 'timestamp', lookup_expr = 'lt')
    timestamp__gt = django_filters.DateTimeFilter(name = 'timestamp', lookup_expr = 'gt')
    finalized = django_filters.BooleanFilter()
    class Meta:
        model = Roll
        fields = ['id','status','finalized','notes','timestamp','event','trainee','monitor']

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