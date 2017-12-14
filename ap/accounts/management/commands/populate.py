from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
  def handle(self, *args, **options):

    # independent models
    call_command('populate_localities')
    call_command('populate_teams')
    call_command('populate_tas')
    call_command('populate_houses')
    call_command('populate_rooms')
    call_command('populate_terms')
    call_command('populate_books')

    # dependent models
    call_command('populate_trainees')
    call_command('populate_events')
    call_command('populate_schedules') # depends on event and trainee population
    call_command('populate_rolls')
    call_command('populate_services')
    call_command('populate_biblereading')
    call_command('populate_lifestudies')
    call_command('populate_leaveslips')

    print('You may now want to manage permissions/groups or create a superuser: ./manage.py createsuperuser')
