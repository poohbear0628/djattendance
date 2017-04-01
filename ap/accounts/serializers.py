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
    events = AttendanceEventWithDateSerializer(many=True,)
    class Meta:
        model = Trainee
        exclude = ['password']
    def get_trainee_name(self, obj):
        return obj.__unicode__()

class TraineeForAttendanceSerializer(BulkSerializerMixin, ModelSerializer):
    list_serializer_class = BulkListSerializer
    name = SerializerMethodField('get_trainee_name')
    class Meta:
        model = Trainee
        fields = ['id', 'terms_attended', 'firstname', 'lastname', 'groups', 'name', 'team']
    def get_trainee_name(self, obj):
        return obj.firstname + ' ' + obj.lastname

class TrainingAssistantSerializer(BulkSerializerMixin, ModelSerializer):
    list_serializer_class = BulkListSerializer
    class Meta:
        model = TrainingAssistant
        fields = ['id', 'email', 'firstname', 'lastname', 'middlename', 'gender']

class TraineeRollSerializer(ModelSerializer):
	class Meta:
		model = Trainee
		fields = ['id', 'type', 'firstname', 'lastname', 'middlename', 'gender', 'self_attendance', 'current_term']
