from django.db import models
from accounts.models import Trainee

class Announcement(models.Model):

    ANNOUNCE_STATUS = (
        ('A', 'Approved'),
        ('P', 'Pending'),
        ('F', 'Fellowship'),
        ('D', 'Denied'),
        ('S', 'TA sister approved')
    )

    ANNOUNCE_TYPE = (
        ('CLASS', 'In-class'),
        ('SERVE', 'On the server')
    )

    status = models.CharField(max_length=1, choices=ANNOUNCE_STATUS, default='P')
    type = models.CharField(max_length=1, choices=ANNOUNCE_TYPE, default='CLASS')

    # date the request was made
    date_requested = models.DateTimeField(auto_now_add=True)

    # trainee who submitted the request
    trainee = models.ForeignKey(Trainee, null=True)

    # TA comments
    comments = models.TextField()
    

