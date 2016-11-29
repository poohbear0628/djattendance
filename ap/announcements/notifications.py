import datetime

from django.contrib import messages
from django.db.models import Count, Q

from models import Announcement
from aputils.trainee_utils import is_trainee, trainee_from_user

def get_announcements(request):
    notifications = []
    if is_trainee(request.user):
        trainee = trainee_from_user(request.user)
        notifications.extend(discipline_announcements(trainee))
        notifications.extend(server_announcements(trainee))
    return notifications

def server_announcements(trainee):
    today = datetime.date.today()
    announcements = Announcement.objects \
        .annotate(num_trainees=Count('trainees')) \
        .filter(Q(type='SERVE') & \
            Q(status='A') & \
            Q(announcement_date__lte=today) & \
            Q(announcement_end_date__gte=today) & \
            (Q(num_trainees=0) | Q(trainees=trainee)))
    return [(messages.INFO, a.announcement) for a in announcements]

def discipline_announcements(trainee):
    notifications = []
    for discipline in trainee.discipline_set.all():
        if discipline.get_num_summary_due() > 0:
            content = 'Life Study Summary due for {infraction}. <a href="/lifestudies">Still need: {due}</a>'.format(infraction=discipline.get_infraction_display(), due=discipline.get_num_summary_due())
            notifications.append((messages.WARNING, content))
    return notifications
