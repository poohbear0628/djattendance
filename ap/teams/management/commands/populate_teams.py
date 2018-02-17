from django.core.management.base import BaseCommand
from teams.models import Team
from localities.models import Locality
from aputils.models import City


def new_team(teams=[], ty="CAMPUS"):
  for team in teams:
      c, made = City.objects.get_or_create(name=team[2], state="CA")
      loc, made = Locality.objects.get_or_create(city=c)

      t = Team(name=team[0], code=team[1], type=ty, locality=loc)
      t.save()


class Command(BaseCommand):
  # to use: python ap/manage.py populate_teams --settings=ap.settings.dev
  def _create_teams(self):

      teams = [("Cal Poly Pomona","CPP", "Diamond Bar"), ("Cal State University Fullerton","CSUF", "Fullerton"), ("Cal State University Los Angeles","CSULA", "Los Angeles"), ("Cerritos College","CRC", "Cerritos"), ("Chapman College","CHAP", "Orange"), ("Cypress College","CC", "Cypress"), ("Fullerton College","FC", "Fullerton"), ("Mount San Antonio College","MSC", "Diamond Bar"), ("Orange Coast College","OCC", "Orange"), ("Saddleback College","SC", "San Juan Capistrano"), ("Santa Ana College","SAC", "Santa Ana"), ("University of California Irvine","UCI", "Irvine"), ("University of California, Los Angeles","UCLA", "Los Angeles"), ("University of Southern California","USC", "Los Angeles"), ("East LA College","ELAC", "East LA"), ("Long Beach","LB", "Long Beach"), ("Pasadena City College","PCC", "Pasedena"), ("California Institute of Technology","CIT", "Pasedena"), ("Santiago Canyon College","SCC", "Orange"), ("University of California Riverside","UCR", "Riverside")]
      new_team(teams, 'CAMPUS')

      teams = [("Children - Anaheim","CH-ANA", "Anaheim"), ("Children - Fullerton","CH-FUL", "Fullerton"), ("Children - Irvine","CH-IRV", "Irvine"), ("Children - Orange","CH-OR", "Orange"), ("Children - Santa Ana","CH-SA", "Santa Ana"), ("Children - Diamond Bar","CH-DB", "Diamond Bar"), ("Children - San Juan Capistrano","CH-SJC", "San Juan Capistrano"), ("Children - Lake Forest","CH-LF", "Lake Forest"), ("Children - Cypress","CH-CYP", "Cypress")]
      new_team(teams, 'CHILD')

      teams = [("Community - Anaheim","COM-ANA", "Anaheim"), ("Community - Diamond Bar","COM-DB", "Diamond Bar"), ("Community - Fullerton","COM-FUL", "Fullerton"), ("Community - Irvine","COM-IRV", "Irvine"), ("Community - Orange","COM-OR", "Orange"), ("Community - Cerritos","COM-CER", "Cerritos"), ("Community - Anaheim D1","COM-ANA1", "Anaheim"), ("Community - Anaheim D2","COM-ANA2", "Anaheim"), ("Community - Anaheim D3","COM-ANA3", "Anaheim"), ("Community - Anaheim D4","COM-ANA4", "Anaheim"), ("Community - Anaheim D5","COM-ANA5", "Anaheim")]
      new_team(teams, 'COM')

      teams = [("Young People - Anaheim","YP-ANA", "Anaheim"), ("Young People - Diamond Bar","YP-DB", "Diamond Bar"), ("Young People - Fullerton","YP-FUL", "Fullerton"), ("Young People - Huntington Beach","YP-HB", "Huntington Beach"), ("Young People - Irvine","YP-IRV", "Irvine"), ("Young People - Cerritos","YP-CER", "Cerritos"), ("Young People - Long Beach","YP-LB", "Long Beach"), ("Young People - San Juan Capistrano","YP-SJC", "San Juan Capistrano"), ("Young People - Walnut","YP-WAL", "Walnut"), ("Young People - Santa Ana","YP-SA", "Santa Ana"), ("Young People - Eastvale","YP-EV", "Eastvale")]
      new_team(teams, 'YP')

      ana = ["Community - Anaheim D1", "Community - Anaheim D2", "Community - Anaheim D3", "Community - Anaheim D4", "Community - Anaheim D5"]

      for a in ana:
        t = Team.objects.get(name=a)
        t.superteam = Team.objects.get(name="Community - Anaheim")
        t.save()

  def handle(self, *args, **options):
    Team.objects.all().delete()
    City.objects.all().delete()
    print("* Populating teams...")
    self._create_teams()
