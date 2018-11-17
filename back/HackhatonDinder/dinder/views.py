from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dinder.models import DinderEvent, DinderProfile
from dinder.serializers import GroupSerializer, EventSerializer, ProfileSerializer


def index(request):
    return HttpResponse("Dinder home.")


@api_view(['GET'])
def loginView(request, username):
    print('not implemented login')

    return Response({
        'success': True,
        'token': 'RanDoMToKe'
    })


@api_view(['GET'])
def logoutView(request, username):
    print('not implemented logout')

    return Response({
        'success': True
    })


@api_view(['GET'])
def showGroups(request, userid):
    guy = DinderProfile.objects.get(id=userid)
    guy_groups = guy.groups.all()
    serializer = GroupSerializer(guy_groups, many=True)

    return Response({
        'success': True,
        'groups': serializer.data
    })


@api_view(['GET'])
def showEvents(request, userid, groupname):
    guy = DinderProfile.objects.get(id=userid)
    guy_groups = guy.groups.all()
    group = guy_groups.get(name=groupname)
    events = group.dinderevent_set.all()

    serializer = EventSerializer(events, many=True)

    return Response({
        'success': True,
        'events': serializer.data
    })


@api_view(['GET'])
def showPeopleOfEvent(request, userid, groupname, eventid):
    guy = DinderProfile.objects.get(id=userid)
    guy_groups = guy.groups.all()
    group = guy_groups.get(name=groupname)
    events = group.dinderevent_set.all()
    event = events.get(id=eventid)
    people = (event.dinderprofile_set.all())
    people_serializer = ProfileSerializer(people, many=True)

    return Response({
        'success': True,
        'name': event.name,
        'location': event.localization,
        'taken': len(people),
        'total': 999,
        'people': people_serializer.data
    })
