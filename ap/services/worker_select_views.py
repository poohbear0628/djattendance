from accounts.views import TraineesByGender, TraineesByHouse, TraineesByLocality, TraineesByTeam, TraineesByTerm, TraineesByTeamType, TraineesHouseCoordinators
from accounts.serializers import TraineeSerializer
from services.models.worker import Worker

from itertools import chain


class WorkerSerializer(TraineeSerializer):

  class Meta(TraineeSerializer.Meta):
    model = Worker
    fields = ['id', 'health', 'services_cap']

  def get_trainee_name(self, obj):
    return '%s %s' % (obj.trainee.firstname, obj.trainee.lastname)


class WorkerMixin:
  serializer_class = WorkerSerializer

  def get_queryset(self):
    qs = super(WorkerMixin, self).get_queryset()
    w = Worker.objects.none()
    for t in qs:
      w = chain(w, t.worker)
    return w


class WorkersByGender(TraineesByGender, WorkerMixin):
  pass


class WorkersByHouse(TraineesByHouse, WorkerMixin):
  pass


class WorkersByLocality(TraineesByLocality, WorkerMixin):
  pass


class WorkersByTeam(TraineesByTeam, WorkerMixin):
  pass


class WorkersByTerm(TraineesByTerm, WorkerMixin):
  pass


class WorkersByTeamType(TraineesByTeamType, WorkerMixin):
  pass


class WorkersHouseCoordinators(TraineesHouseCoordinators, WorkerMixin):
  pass
