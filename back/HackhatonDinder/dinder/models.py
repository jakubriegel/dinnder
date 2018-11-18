from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class DinderGroup(models.Model):
    name = models.CharField(max_length=100)
    is_private = models.BooleanField(default=False)
    image = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.id) + ' ' + self.name


class DinderEvent(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey(DinderGroup,on_delete=models.CASCADE)
    localizationName = models.CharField(max_length=100,null=True,blank=True)
    localizationLNG = models.FloatField(null=True,blank=True)
    localizationLAT = models.FloatField(null=True,blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    dateOfEvent = models.DateTimeField(default = datetime.now, blank=True)

    limitOfPeople = models.IntegerField(default=5)
    def __str__(self):
        return "id: "+str(self.id) + ' '+self.name + ' '+' | grupa: '+str(self.group.name)


class DinderProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=50)
    image = models.CharField(max_length=500, null=True, blank=True)
    groups = models.ManyToManyField(DinderGroup, null=True, blank=True)
    events = models.ManyToManyField(DinderEvent, null=True, blank=True)
    localizationLNG = models.FloatField(null=True, blank=True)
    localizationLAT = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.surname
