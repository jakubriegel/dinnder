from rest_framework import serializers

from dinder import models


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DinderGroup
        fields = ('id', 'name', 'is_private','description')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = models.DinderEvent
        fields = ('id', 'name', 'group', 'localizationName','localizationLNG','localizationLAT',
                  'description','dateOfEvent','limitOfPeople')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = models.DinderProfile
        fields = ('id', 'name', 'surname', 'username', 'image', 'groups', 'events', 'localizationLNG', 'localizationLAT')
