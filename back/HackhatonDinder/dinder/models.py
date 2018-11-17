from django.db import models

# Create your models here.

class DinderGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DinderEvent(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(DinderGroup,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class DinderProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    groups = models.ManyToManyField(DinderGroup,null=True,blank=True)
    events = models.ManyToManyField(DinderEvent,null=True,blank=True)
    def __str__(self):
        return self.name +' ' +self.surname
