from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
  def handle(self, *args, **options):
    call_command('populate_terms')
    call_command('populate_events')
    call_command('populate_schedules')
    call_command('populate_trainees')
    call_command('populate_tas')
    call_command('populate_rolls')
    call_command('populate_services')
