import django_filters
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Roll
from rest_framework import serializers, filters
from accounts.models import Trainee
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
    schedule = ScheduleSerializer(many=True,)
    class Meta(object):
   		model = Trainee
   		list_serializer_class = BulkListSerializer
   		fields = '__all__'
    def get_trainee_name(self, obj):
        return obj.__unicode__()

class AttendanceFilter(filters.FilterSet):
	class Meta:
		model = Trainee
		fields = ['id','individualslips','groupslips','rolls','schedule','term']