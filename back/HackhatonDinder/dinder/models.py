from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class DinderGroup(models.Model):
    name = models.CharField(unique=True,max_length=100)
    is_private=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' '+self.name



class DinderEvent(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(DinderGroup,on_delete=models.CASCADE)
    localization = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.id) + ' '+self.name


class DinderProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(unique=True,max_length=50)
    image = models.CharField(max_length=500,null=True,blank=True)
    groups = models.ManyToManyField(DinderGroup,null=True,blank=True)
    events = models.ManyToManyField(DinderEvent,null=True,blank=True)
    localization = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.id) + ' '+self.name +' ' +self.surname
