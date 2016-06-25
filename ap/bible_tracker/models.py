from django.db import models
from django.contrib.postgres.fields import HStoreField
from accounts.models import User
import json

class BibleReading(models.Model):
	trainee = models.ForeignKey(User, null=True)
	weekly_reading_status = HStoreField()
	books_read = HStoreField()

	def weekly_statistics(self, start_week, end_week, term_id):

		stats = {'firstname': self.trainee.firstname, 'lastname': self.trainee.lastname, 'current_term': self.trainee.current_term, 'number_complete': 0, 'percent_complete': 0, 'number_madeup': 0, 'percent_madeup': 0,'number_notread': 0, 'percent_notread': 0,'number_blank': 0, 'percent_blank': 0,'number_complete_madeup': 0, 'percent_complete_madeup': 0, 'percent_firstyear': 0, 'percent_secondyear': 0}

		multiple_weeks_stats = []
		
		for x in range(start_week, end_week + 1):
			if str(term_id) + "_" + str(x) in self.weekly_reading_status:
				print str(term_id) + "_" + str(x)
				trainee_weekly_reading = self.weekly_reading_status[str(term_id) + "_" + str(x)]
				json_weekly_reading = json.loads(trainee_weekly_reading)
				weekly_status = json_weekly_reading['status']
				trainee_stats = stats.copy()

				trainee_stats['number_complete'] = weekly_status.count('C')
				trainee_stats['percent_complete'] = (weekly_status.count('C')/7.0) *100.0
				trainee_stats['number_madeup'] = weekly_status.count('M')
				trainee_stats['percent_madeup'] = (weekly_status.count('M')/7.0) *100.0
				trainee_stats['number_notread'] = weekly_status.count('N')
				trainee_stats['percent_notread'] = (weekly_status.count('N')/7.0) *100.0
				trainee_stats['number_blank'] = weekly_status.count('_')
				trainee_stats['percent_blank'] = (weekly_status.count('_')/7.0) *100.0
				trainee_stats['number_complete_madeup'] = weekly_status.count('C') + weekly_status.count('M')
				trainee_stats['percent_complete_madeup'] = ((weekly_status.count('C') + weekly_status.count('M'))/7.0) *100.0
				multiple_weeks_stats.append(trainee_stats)

		if multiple_weeks_stats:
			final_stats = stats.copy()

			final_stats['number_complete'] = sum(week_stats['number_complete'] for week_stats in multiple_weeks_stats)
			final_stats['percent_complete'] = int(sum(week_stats['percent_complete'] for week_stats in multiple_weeks_stats) / float(len(multiple_weeks_stats)))
			final_stats['number_madeup'] = sum(week_stats['number_madeup'] for week_stats in multiple_weeks_stats)
			final_stats['percent_madeup'] = int(sum(week_stats['percent_madeup'] for week_stats in multiple_weeks_stats) / float(len(multiple_weeks_stats)))
			final_stats['number_notread'] = sum(week_stats['number_notread'] for week_stats in multiple_weeks_stats)
			final_stats['percent_notread'] = int(sum(week_stats['percent_notread'] for week_stats in multiple_weeks_stats)/ float(len(multiple_weeks_stats)))	 
			final_stats['number_blank'] = sum(week_stats['number_blank'] for week_stats in multiple_weeks_stats)
			final_stats['percent_blank'] = int(sum(week_stats['percent_blank'] for week_stats in multiple_weeks_stats) / float(len(multiple_weeks_stats)))	 
			final_stats['number_complete_madeup'] = sum(week_stats['number_complete'] for week_stats in multiple_weeks_stats) + sum(week_stats['number_madeup'] for week_stats in multiple_weeks_stats)
			final_stats['percent_complete_madeup'] = int(((sum(stats['percent_complete'] for week_stats in multiple_weeks_stats) + sum(week_stats['number_madeup'] for week_stats in multiple_weeks_stats)) / float(len(multiple_weeks_stats))))	
			# final_stats['percent_secondyear'] = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('1_')]
			return final_stats
		else:
			return stats








		
	   
