from rest_framework.serializers import ModelSerializer, SerializerMethodField
from schedules.serializers import AttendanceEventWithDateSerializer
from .models import User, Trainee, TrainingAssistant
from rest_framework_bulk import (
  BulkListSerializer,
  BulkSerializerMixin
)


class BasicUserSerializer(BulkSerializerMixin, ModelSerializer):
  list_serializer_class = BulkListSerializer

  class Meta:
    model = User
    fields = ['id', 'firstname', 'lastname', 'full_name']


class UserSerializer(BulkSerializerMixin, ModelSerializer):
  list_serializer_class = BulkListSerializer

  class Meta:
    model = User


class TraineeSerializer(BulkSerializerMixin, ModelSerializer):
  list_serializer_class = BulkListSerializer
  name = SerializerMethodField('get_trainee_name')

  class Meta:
    model = Trainee
    fields = ['id', 'name', 'type', 'rfid_tag', 'firstname', 'lastname', 'gender', 'current_term', 'TA', 'mentor', 'team', 'house', 'groups', 'terms_attended', 'locality']

  def get_trainee_name(self, obj):
    return '%s %s' % (obj.firstname, obj.lastname)


class TraineeForAttendanceSerializer(BulkSerializerMixin, ModelSerializer):
  list_serializer_class = BulkListSerializer
  name = SerializerMethodField('get_trainee_name')

  class Meta:
    model = Trainee
    fields = ['id', 'firstname', 'self_attendance', 'lastname', 'groups', 'name', 'team', 'TA']

  def get_trainee_name(self, obj):
    return '%s %s' % (obj.firstname, obj.lastname)


class TrainingAssistantSerializer(BulkSerializerMixin, ModelSerializer):
  list_serializer_class = BulkListSerializer
  name = SerializerMethodField('get_ta_name')

  class Meta:
    model = TrainingAssistant
    fields = ['id', 'email', 'firstname', 'lastname', 'middlename', 'gender', 'name']

  def get_ta_name(self, obj):
    return '%s %s' % (obj.firstname, obj.lastname)


class TraineeRollSerializer(ModelSerializer):

  class Meta:
    model = Trainee
    fields = ['id', 'type', 'firstname', 'lastname', 'middlename', 'gender', 'self_attendance', 'current_term']
