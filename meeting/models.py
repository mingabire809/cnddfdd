from django.db import models


# Create your models here.
from antenne.models import Antenne
from member.models import Member


class Meeting(models.Model):
    meetingName = models.CharField(verbose_name='Meeting', max_length=150, primary_key=True)
    antenne = models.ForeignKey(Antenne,verbose_name='Antenne', on_delete=models.CASCADE)
    place = models.CharField(verbose_name='Place', max_length=150)
    date = models.DateTimeField(verbose_name="Time")
    members = models.ManyToManyField(Member,verbose_name='Member Concerned',related_name=antenne)

    def __str__(self):
        return f'{self.meetingName}, {self.antenne}, {self.place}, {self.date}, {self.members}'


