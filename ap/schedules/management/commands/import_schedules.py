import csv
import os
from datetime import datetime

from django.core.management.base import BaseCommand

from schedules.models import Schedule, Event
from terms.models import Term


"""
To generate schedule.csv:
SELECT schedule.ID, schedule.name, comments, startDate, endDate, termID, scheduleCategory.name, priority, display
FROM `schedule`, `scheduleCategory` WHERE termID=26 and scheduleCategoryID=scheduleCategory.ID

To generate event.csv:
SELECT * FROM `scheduleEvent` WHERE scheduleID in ('5712', '5735', '5767', '5785', '5852', '5875', '5907', '5925', '5929', '5934', '5647', '5648', '5650', '5651', '5652', '5653', '5654', '5655', '5656', '5657', '5659', '5660', '5661', '5663', '5664', '5665', '5666', '5667', '5668', '5669', '5670', '5671', '5672', '5673', '5674', '5675', '5676', '5677', '5678', '5679', '5680', '5681', '5682', '5683', '5684', '5685', '5686', '5687', '5688', '5689', '5690', '5691', '5692', '5693', '5695', '5696', '5697', '5698', '5699', '5700', '5701', '5702', '5703', '5704', '5738', '5740', '5747', '5748', '5750', '5751', '5753', '5758', '5760', '5761', '5762', '5763', '5764', '5765', '5766', '5770', '5771', '5772', '5773', '5776', '5777', '5782', '5783', '5784', '5786', '5787', '5788', '5790', '5791', '5792', '5793', '5794', '5795', '5796', '5797', '5799', '5800', '5801', '5803', '5804', '5805', '5806', '5807', '5808', '5809', '5810', '5811', '5812', '5813', '5814', '5815', '5816', '5817', '5818', '5819', '5820', '5821', '5822', '5823', '5824', '5825', '5826', '5827', '5828', '5829', '5830', '5831', '5832', '5833', '5835', '5836', '5837', '5838', '5839', '5840', '5841', '5842', '5843', '5844', '5878', '5880', '5887', '5888', '5890', '5891', '5893', '5898', '5900', '5901', '5902', '5903', '5904', '5905', '5906', '5910', '5911', '5912', '5913', '5916', '5917', '5922', '5923', '5924', '5926', '5713', '5734', '5737', '5853', '5874', '5877', '5932', '5705', '5706', '5707', '5708', '5709', '5710', '5723', '5731', '5739', '5743', '5752', '5775', '5778', '5779', '5780', '5845', '5846', '5847', '5848', '5849', '5850', '5863', '5871', '5879', '5883', '5892', '5915', '5918', '5919', '5920', '5928', '5933', '5714', '5736', '5745', '5755', '5756', '5757', '5759', '5774', '5781', '5854', '5876', '5885', '5895', '5896', '5897', '5899', '5914', '5921', '5927', '5930', '5716', '5717', '5718', '5719', '5720', '5721', '5722', '5726', '5727', '5728', '5729', '5742', '5856', '5857', '5858', '5859', '5860', '5861', '5862', '5866', '5867', '5868', '5869', '5882', '5658', '5694', '5715', '5724', '5725', '5732', '5733', '5741', '5744', '5746', '5754', '5798', '5834', '5855', '5864', '5865', '5872', '5873', '5881', '5884', '5886', '5894', '5711', '5730', '5749', '5851', '5870', '5889', '5768', '5908', '5931', '5649', '5662', '5769', '5789', '5802', '5909')
"""
SCHEDULE_FILE = 'ap/schedules/management/schedule.csv'
EVENT_FILE = 'ap/schedules/management/event.csv'
ROLL_TYPES = set(['House Roll', 'Team Roll', 'Meal Roll', 'Class Roll', 'Study Roll', 'YPC - All'])


class Command(BaseCommand):
  def _create_schedules(self):
    schedule_file = open(SCHEDULE_FILE)
    event_file = open(EVENT_FILE)
    current_term = Term.current_term()
    schedule_categories = {}

    for row in csv.DictReader(schedule_file):
      if Schedule.objects.filter(name=row['name'], comments=row['comments']).exists():
        continue
      start_date = datetime.strptime(row['startDate'], "%Y-%m-%d").date()
      end_date = datetime.strptime(row['endDate'], "%Y-%m-%d").date()
      start_week = current_term.term_week_of_date(start_date)
      end_week = current_term.term_week_of_date(end_date)
      weeks = ','.join([str(w) for w in range(start_week, end_week + 1)])
      schedule_categories[row['ID']] = row['category']
      s = Schedule(id=row['ID'], name=row['name'], comments=row['comments'],
                   season='All', weeks=weeks, import_to_next_term=True,
                   term=current_term, priority=int(row['priority']))
      s.save()

    for row in csv.DictReader(event_file):
      if not row['name'] and not row['code']:  # don't import exceptions
        continue
      if not Schedule.objects.filter(id=row['scheduleID']):
        continue
      schedule = Schedule.objects.get(id=row['scheduleID'])
      event_type = schedule_categories[row['scheduleID']][0] if schedule_categories[row['scheduleID']] in ROLL_TYPES else '*'
      event = Event(weekday=int(row['weekDayID']) - 1, name=row['name'],
                    code=row['code'], start=row['startTime'], end=row['endTime'],
                    type=event_type)
      event.save()
      schedule.events.add(event)

  def handle(self, *args, **options):
    if os.path.isfile(SCHEDULE_FILE) and os.path.isfile(EVENT_FILE):
      Schedule.objects.all().delete()
      Event.objects.all().delete()
      print("* Populating schedules...")
      self._create_schedules()
    else:
      print('No import files found')
