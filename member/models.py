from django.db import models


# Create your models here.
from antenne.models import Antenne


class Member(models.Model):
    firstName = models.CharField(verbose_name='First Name', max_length=60)
    lastName = models.CharField(verbose_name='Last Name', max_length=60)
    phoneNumber = models.IntegerField(verbose_name='Phone Number', unique=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True, primary_key=True)
    antenne = models.ForeignKey(Antenne, verbose_name='Antenne belonging to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}, {self.phoneNumber}, {self.firstName}, {self.antenne}'
