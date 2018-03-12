from django.core.management.base import BaseCommand
from accounts.models import Trainee
from teams.models import Team
from django.core.exceptions import ObjectDoesNotExist
import xlrd


# run from commands folder: ../../../manage.py update_teams
class Command(BaseCommand):
  def handle(self, *args, **options):
    book = xlrd.open_workbook("S18 Attendance Import 03.02.18.xlsx")
    sheet = book.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):  # Iterate through rows
      cell_obj_email = sheet.cell(row_idx, 16)  # Get cell object by row, col
      cell_obj_team = sheet.cell(row_idx, 40)  # Get cell object by row, col
      cell_email = cell_obj_email.value  # Get cell value
      cell_team = cell_obj_team.value  # Get cell value

      try:
        tr = Trainee.objects.get(email=cell_email)
      except ObjectDoesNotExist:
        print('Person associated with email: [%s] was not found' % cell_email)

      try:
        te = Team.objects.get(code=cell_team)
        tr.team = te
        tr.save()
      except ObjectDoesNotExist:
        print('The team [%s] does not exist for: [%s %s]' % (cell_team, tr.firstname, tr.lastname))
