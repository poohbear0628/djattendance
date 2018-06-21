from datetime import datetime

from aputils.trainee_utils import is_trainee

from .models import GospelTrip


def gospel_trips_available(request):
  user = request.user
  if not hasattr(user, 'type') or not is_trainee(user):
    return {'gospel_trips_available': False}

  try:
    admin = GospelTrip.objects.order_by('open_time').first()
    if admin.open_time:
        if datetime.now() < admin.open_time:
          return {'gospel_trips_available': False}
    elif admin.close_time:
      if datetime.now() > admin.close_time:
        return {'gospel_trips_available': False}
    return {'gospel_trips_available': True}
  except GospelTrip.DoesNotExist:
    return {'gospel_trips_available': False}
