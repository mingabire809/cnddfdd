from django.db import models

# Create your models here.
from member.models import Member


class Event(models.Model):
    eventName = models.CharField(verbose_name='The event name', max_length=100, primary_key=True)
    location = models.CharField(verbose_name='Place', max_length=150)
    date = models.DateField(verbose_name='Date of the event')
    program = models.CharField(verbose_name='program of the event', max_length=150)
    participant = models.ManyToManyField(Member)

    def __str__(self):
        return f'{self.eventName}, {self.location}, {self.date}, {self.program}, {self.participant}'
