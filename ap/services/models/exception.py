from django.db import models

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
    end = models.DateField(null=True, blank=True)

    # whether this exception is in effect or not
    active = models.BooleanField(default=True)

    trainees = models.ManyToManyField('Worker', related_name="exceptions")
    services = models.ManyToManyField('Service')

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
