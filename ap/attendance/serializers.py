from rest_framework.serializers import ModelSerializer
from .models import Roll
from rest_framework import serializers
from accounts.models import Trainee
from leaveslips.serializers import IndividualSlipSerializer, GroupSlipSerializer
class RollSerializer(ModelSerializer):
    class Meta:
        model = Roll

class AttendanceSerializer(ModelSerializer):
    individualslips = IndividualSlipSerializer(many=True, read_only=True)
    groupslips = GroupSlipSerializer(many=True, read_only=True)
    class Meta:
   		model = Trainee

