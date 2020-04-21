from django.db import models
from people.models import People



class OurCalendar(models.Model):
    man = models.ForeignKey(People, related_name='our_calendars', on_delete=models.DO_NOTHING)
    data_start = models.DateField(null=True, blank=True)
    data_finish = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.man)

    def res(self):
        return self.data_finish - self.data_start
