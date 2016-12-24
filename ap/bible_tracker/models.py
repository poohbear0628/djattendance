from django.db import models
from django.contrib.postgres.fields import HStoreField
from accounts.models import Trainee
import json

class BibleReading(models.Model):
  trainee = models.ForeignKey(Trainee, null=True)
  weekly_reading_status = HStoreField()
  books_read = HStoreField()

  def weekly_statistics(self, start_week, end_week, term_id):
    trainee_stats = {'firstname': self.trainee.firstname, 'lastname': self.trainee.lastname, 'current_term': self.trainee.current_term}

    number_complete = 0
    number_madeup = 0
    number_notread = 0
    number_blank = 0
    number_complete_madeup = 0
    number_days = float((end_week - start_week +1) *7)

    for week in range(start_week, end_week + 1):
      term_week_id = str(term_id) + "_" + str(week)
      if term_week_id in self.weekly_reading_status:
        trainee_weekly_reading = self.weekly_reading_status[term_week_id]
        json_weekly_reading = json.loads(trainee_weekly_reading)
        weekly_status = json_weekly_reading['status']
        # Counts number of days in week with (C)omplete, (M)adeup, (_)Blank , and (C+M)Complete + Madeup
        number_complete += weekly_status.count('C')
        number_madeup += weekly_status.count('M')
        number_notread += weekly_status.count('N')
        number_blank += weekly_status.count('_')
        number_complete_madeup += (weekly_status.count('C') + weekly_status.count('M'))

    # Calculates percentages and adds to stats dictionary, along with final counts
    trainee_stats['number_complete'] = number_complete
    trainee_stats['percent_complete'] = int((number_complete/number_days) *100)
    trainee_stats['number_madeup'] = number_madeup
    trainee_stats['percent_madeup'] = int((number_madeup/number_days) * 100)
    trainee_stats['number_notread'] = number_notread
    trainee_stats['percent_notread'] = int((number_notread/number_days) *100)
    trainee_stats['number_blank'] = number_blank
    trainee_stats['percent_blank'] = int((number_blank/number_days) * 100)
    trainee_stats['number_complete_madeup'] = number_complete_madeup
    trainee_stats['percent_complete_madeup'] = int((number_complete_madeup/number_days) *100)

    return trainee_stats










