from rest_framework.serializers import ModelSerializer, SerializerMethodField
from schedules.serializers import AttendanceEventWithDateSerializer
from .models import User, Trainee, TrainingAssistant

class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class TraineeSerializer(ModelSerializer):
	name = SerializerMethodField('get_trainee_name')
	events = AttendanceEventWithDateSerializer(many=True,)
	class Meta:
		model = Trainee

	def get_trainee_name(self, obj):
		return obj.__unicode__()

class TrainingAssistantSerializer(ModelSerializer):
    class Meta:
        model = TrainingAssistant

class TraineeRollSerializer(ModelSerializer):
	class Meta:
		model = Trainee
		fields = ['id', 'type', 'firstname', 'lastname', 'middlename', 'gender', 'self_attendance', 'current_term']