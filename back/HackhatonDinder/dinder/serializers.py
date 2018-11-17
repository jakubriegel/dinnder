from rest_framework import serializers

from dinder import models


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DinderEvent
        fields = ('name',)
