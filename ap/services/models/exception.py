from django.db import models


# TODO: UI represent as time blocks -> translate into services blocked out
# TODO: Should exceptions handle time block conflict checking in addition 
# to just service blocking?
class Exception(models.Model):
    """
    Defines an ineligibility rule for workers to certain services.
    """

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    start = models.DateField()
    # some exceptions are just evergreen
    # UI will give 3 options, definite date, end of term, permanent (empty)
    end = models.DateField(null=True, blank=True)

    # whether this exception is in effect or not
    active = models.BooleanField(default=True)

    trainees = models.ManyToManyField('Worker', related_name="exceptions")
    services = models.ManyToManyField('Service')

    last_modified = models.DateTimeField(auto_now=True)

    def checkException(self, worker, instance):
        if instance.service in self.services:
            return False
        else:
            return True

    def get_absolute_url(self):
        return "/ss/exceptions/%i/" % self.id

    def __unicode__(self):
        return self.name


# TODO: ExceptionRequest (request for exception to be added instead of a handwritten note to schedulers)
