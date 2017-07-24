from django.core.management.base import BaseCommand
from rooms.models import Room

class Command(BaseCommand):
  # to use: python ap/manage.py populate_rooms --settings=ap.settings.dev

  def _create_room(self, room):
    print room['code']
    r = Room(code=room['code'], name=room['name'], floor=1, type=room['type'], access=room['access'], reservable=True)
    r.save()
    return r

  def _create_rooms(self):
    all_rooms = ['MC', 'NE209', 'NE210', 'NE212', 'NE215', 'NE216',
    'NE217', 'NE218', 'NE219', 'NE220', 'NE221', 'NE222', 'NE223', 'NE224', 'NE225', 'NE3',
    'NW201', 'SE132', 'SE238', 'SE239', 'SE240', 'SE241', 'SE243', 'SE244', 'SE245', 'SE227', 'SW229']
    b_rooms = ['SE238', 'SE239', 'SE240', 'SE241', 'SE242', 'SE243', 'SE244', 'SE245']
    s_rooms = ['NE209', 'NE210', 'NE212', 'NE213', 'NE215', 'NE216', 'NE217', 'NE218',
    'NE219', 'NE220', 'NE221', 'NE222', 'NE223', 'NE224', 'NE225']

    rooms = []
    for room in all_rooms:
      rooms.append(
        {'code': room,
        'name': room,
        'type':'SR',
        'access': 'C',
        }
      )
    for room in rooms:
      r = self._create_room(room)
      if r.name in b_rooms:
        r.access = 'B'
      if r.name in s_rooms:
        r.access = 'S'
      r.save()
    print 'done'

  def handle(self, *args, **options):
    self._create_rooms()
