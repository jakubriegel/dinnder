from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dinder.models import DinderEvent, DinderProfile
from dinder.serializers import GroupSerializer, EventSerializer, ProfileSerializer
from geopy.distance import geodesic

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
def showEvents(request, userid, groupid):
    guy = DinderProfile.objects.get(id=userid)
    guy_groups = guy.groups.all()
    group = guy_groups.get(id=groupid)
    events = group.dinderevent_set.all()

    serializer = EventSerializer(events, many=True)
    return Response({
        'success': True,
        'events': serializer.data
    })


@api_view(['GET'])
def get_nearby(request, userid, lat=52.3993137, lng=16.931586899999957):
    user_loc = (lat, lng)

    groups = DinderGroup.objects.all()
    nearby_events = []
    for group in groups:
        if group.is_private is not True:
            events = group.dinderevent_set.all()
            for event in events:
                if event.localizationLNG and event.localizationLAT:
                    if geodesic(user_loc, (event.localizationLAT, event.localizationLNG)).km < 1:
                        nearby_events.append(event)

    serializer = EventSerializer(nearby_events, many=True)

    return Response({
        'success': True,
        'events': serializer.data
    })


@api_view(['GET'])
def showPeopleOfEvent(request, userid, groupid, eventid):
    guy = DinderProfile.objects.get(id=userid)
    guy_groups = guy.groups.all()
    group = guy_groups.get(id=groupid)
    events = group.dinderevent_set.all()
    event = events.get(id=eventid)
    event_serializer = EventSerializer(event)
    people = (event.dinderprofile_set.all())
    people_serializer = ProfileSerializer(people, many=True)

    return Response({
        'success': True,
        'event': event_serializer.data,
        'people': people_serializer.data
    })



@api_view(['POST'])
@csrf_exempt
def groupMaker(request,userid):
    data = json.loads(request.body.decode("utf-8"))
    group = DinderGroup(name=data['groupname'], image=data['image'], description=data['description'])
    group.save()
    guy = DinderProfile.objects.get(id=int(userid))
    guy.groups.add(group)

    return Response({
        'success': True,
    })


@api_view(['POST'])
@csrf_exempt
def eventMaker(request,userid,groupid):
    data = json.loads(request.body.decode("utf-8"))
    guy = DinderProfile.objects.get(id=int(userid))
    groupofguy = DinderGroup.objects.get(id=int(groupid))
    event = DinderEvent(name=data['eventname'],image=data['image'], group=groupofguy, localizationName=data['localizationName'],
                        localizationLNG= data['localizationLNG'], localizationLAT=data['localizationLAT'],
                        description=data['description'], dateOfEvent=data['dateOfEvent'], limitOfPeople=data['limitOfPeople'])
    event.save()
    guy.events.add(event)

    return Response({
        'success': True,
    })


@api_view(['POST'])
@csrf_exempt
def signupForEvent(request,userid,groupid,eventid_to_take):
    guy = DinderProfile.objects.get(id=userid)
    event=DinderEvent.objects.get(id=eventid_to_take)
    guy.events.add(event)
    return Response({
        'success': True,
    })

@api_view(['GET'])
def myEventsTakePartIn(request, userid):
    guy = DinderProfile.objects.get(id=userid)
    events = guy.events.all()
    serializer = EventSerializer(events, many=True)
    return Response({
        'success': True,
        'events': serializer.data
    })