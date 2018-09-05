from datetime import datetime

from aputils.trainee_utils import is_trainee

from .models import GospelTrip


def gospel_trips_available(request):
  user = request.user
  if not hasattr(user, 'type') or not is_trainee(user):
    return {'gospel_trips_available': False}

  try:
    admin = GospelTrip.objects.order_by('open_time')
    if admin.exists():
      admin = admin.first()
      if admin.open_time and admin.close_time:
        right_now = datetime.now()
        if right_now > admin.open_time and right_now < admin.close_time:
          return {'gospel_trips_available': True}
    return {'gospel_trips_available': False}
  except GospelTrip.DoesNotExist:
    return {'gospel_trips_available': False}
