from django.db import models


# Create your models here.


class Antenne(models.Model):
    name = models.CharField(verbose_name='Antenne', max_length=100, unique=True, primary_key=True)
    county = models.CharField(verbose_name='County', max_length=100)


    def __str__(self):
        return f'{self.name}, {self.county}'
