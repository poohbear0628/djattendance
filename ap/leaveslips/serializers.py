import django_filters
from rest_framework.serializers import ModelSerializer
from .models import IndividualSlip, GroupSlip, LeaveSlip, Roll
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
    def to_internal_value(self, data):
	    internal_value = super(IndividualSlipSerializer, self).to_internal_value(data)
	    date_events = data.get('date_events')
	    internal_value.update({
	        'date_events': date_events
	    })
	    return internal_value
    def create(self, validated_data):
    	trainee = validated_data['trainee']
    	data_rolls = validated_data.pop('rolls')
    	date_events = validated_data.pop('date_events')

    	slip = IndividualSlip.objects.create(**validated_data)

    	# For overriding existing leaveslips
        # Check submitting rolls
        # Check all rolls in all leaveslips for repeating rolls
        # Remove that roll from existing leaveslips or delete if all rolls removed
        for roll in data_rolls:
            for leaveslip in IndividualSlip.objects.order_by('-id'):
                new_slip = leaveslip.rolls.filter(id=roll.id)
                if new_slip:
                    if leaveslip.rolls.exclude(id=roll.id):
                        leaveslip.rolls = leaveslip.rolls.exclude(id=roll.id)
                        leaveslip.save()
                    else:
                        leaveslip.delete()
                    break
        for roll in data_rolls:
            slip.rolls.add(roll) # adds rolls to the leaveslip.
        if date_events:
	        # create rolls for given days and events
	        for d, evs in date_events.items():
		        for ev in evs:
			    	# Check for roll using date and event
			        if not Roll.objects.filter(trainee=trainee, date=d, event=ev):
			    	    # Create dummy roll if it doesn't exist
			    	    event_object = Event.objects.filter(id=ev)[0]
			    	    roll_dict = {'trainee': trainee, 'event': event_object, 'status': 'P', 'submitted_by': trainee, 'date': d}
			    	    newroll = Roll.objects.create(**roll_dict)
			    	    # Add rolls to the leaveslip's rolls
			    	    slip.rolls.add(newroll)
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