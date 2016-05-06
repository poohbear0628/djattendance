import django_filters
from rest_framework.serializers import ModelSerializer
from .models import IndividualSlip, GroupSlip, LeaveSlip
from schedules.models import Event
from rest_framework import serializers, filters
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

class IndividualSlipSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = IndividualSlip
        list_serializer_class = BulkListSerializer
        fields = '__all__'
    def create(self, validated_data):
    	print(self)
    	print(self.data)
    	print(self.context)
    	print(validated_data)
    	data_rolls = validated_data.pop('rolls')
    	slip = IndividualSlip.objects.create(**validated_data)
    	for roll in data_rolls:
    	    slip.rolls.add(roll)
    	return slip

class IndividualSlipFilter(filters.FilterSet):
    submitted__lt = django_filters.DateTimeFilter(name = 'submitted', lookup_expr = 'lt')
    submitted__gt = django_filters.DateTimeFilter(name = 'submitted', lookup_expr = 'gt')
    last_modified__lt = django_filters.DateTimeFilter(name = 'last_modified', lookup_expr = 'lt')
    last_modified__gt = django_filters.DateTimeFilter(name = 'last_modified', lookup_expr = 'gt')
    finalized__lt = django_filters.DateTimeFilter(name = 'finalized', lookup_expr = 'lt')
    finalized__gt = django_filters.DateTimeFilter(name = 'finalized', lookup_expr = 'gt')
    class Meta:
        model = IndividualSlip
        fields = ['id','type','status','submitted','last_modified','finalized','description','comments','texted','informed','TA','trainee','rolls']

class GroupSlipSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = GroupSlip
        list_serializer_class = BulkListSerializer
        fields = '__all__'

class GroupSlipFilter(filters.FilterSet):
    submitted__lt = django_filters.DateTimeFilter(name = 'submitted', lookup_expr = 'lt')
    submitted__gt = django_filters.DateTimeFilter(name = 'submitted', lookup_expr = 'gt')
    last_modified__lt = django_filters.DateTimeFilter(name = 'last_modified', lookup_expr = 'lt')
    last_modified__gt = django_filters.DateTimeFilter(name = 'last_modified', lookup_expr = 'gt')
    finalized__lt = django_filters.DateTimeFilter(name = 'finalized', lookup_expr = 'lt')
    finalized__gt = django_filters.DateTimeFilter(name = 'finalized', lookup_expr = 'gt')
    start__lt = django_filters.DateTimeFilter(name = 'start', lookup_expr = 'lt')
    start__gt = django_filters.DateTimeFilter(name = 'start', lookup_expr = 'gt')
    end__lt = django_filters.DateTimeFilter(name = 'end', lookup_expr = 'lt')
    end__gt = django_filters.DateTimeFilter(name = 'end', lookup_expr = 'gt')

    class Meta:
        model = GroupSlip
        fields = ['id','type','status','submitted','last_modified','finalized','description','comments','texted','informed','start','end','TA','trainee','trainees']