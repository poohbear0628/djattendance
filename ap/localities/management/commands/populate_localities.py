from django.core.management.base import BaseCommand
from localities.models import Locality
from aputils.models import City
from django_countries.fields import CountryField


class Command(BaseCommand):
  # to use: python ap/manage.py populate_teams --settings=ap.settings.dev

  def _create_localities(self):

    cities = ["Los Angeles", "Pasedena", "Anaheim", "Cypress", "Diamond Bar", "Fullerton", "Irvine", "Lake Forest", "Orange", "San Juan Capistrano", "Santa Ana", "Cerritos", "East LA", "Riverside", "Eastvale", "Huntington Beach", "Long Beach", "Walnut"]
    for city in cities:
      obj, created = City.objects.update_or_create(name=city, state="CA")
      Locality.objects.update_or_create(city=obj)

  def handle(self, *args, **options):
    print("* Populating localities and corresponding cities...")
    self._create_localities()
