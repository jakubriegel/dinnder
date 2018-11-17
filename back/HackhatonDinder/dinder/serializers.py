from rest_framework import serializers

from dinder import models


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DinderGroup
        fields = ('name', 'is_private')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = models.DinderEvent
        fields = ('name', 'group', 'localization')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = models.DinderEvent
        fields = ('name', 'surname', 'username', 'image', 'groups', 'events', 'localization')
