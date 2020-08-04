import datetime
import json

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    resources = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    def __str__(self):
        return f"""
                Resources: {self.resources},
                Location: {self.location}"""


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)
    # prediction variable
    Hlat = models.FloatField(default=27.9, null=True)
    Hlong = models.FloatField(default=89.5, null=True)
    MaxSusWind = models.FloatField(default=160, null=True)
    Clat = models.FloatField(default=29.951065, null=True)
    Clong = models.FloatField(default=-90.071533, null=True)
    Pop = models.FloatField(default=445000, null=True)
    Area = models.FloatField(default=350, null=True)
    prediction = models.FloatField(default=0)

    def __str__(self):
        return f"""name: {self.name}"""

class Resources(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    resources = models.CharField(max_length= 1000)
    # comma-separated list
    
    def __str__(self):
        return f"""resources: {self.resources}"""