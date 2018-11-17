from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dinder.models import DinderEvent, DinderProfile
from dinder.serializers import GroupSerializer, EventSerializer, ProfileSerializer


def index(request):
    return HttpResponse("Dinder home.")


# @api_view(['GET'])
# def all_events(request):
#     try:
#         events = DinderEvent.objects.all()
#     except DinderEvent.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = EventSerializer(events, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def loginView(request, username):
    print('not implemented login')

    return HttpResponse("not implemented login")


@api_view(['GET'])
def logoutView(request, username):
    print('not implemented logout')

    return HttpResponse("not implemented logout")


@api_view(['GET'])
def showGroups(request, userid):
    guy = DinderProfile.objects.get(id=userid)
    guyGroups = guy.groups.all()

    serializer = GroupSerializer(guyGroups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def showEvents(request, userid, groupname):
    guy = DinderProfile.objects.get(id=userid)
    guyGroups = guy.groups.all()
    group = guyGroups.get(name=groupname)
    events = group.dinderevent_set.all()

    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def showPeopleOfEvent(request, userid, groupname, eventid):
    guy = DinderProfile.objects.get(id=userid)
    guyGroups = guy.groups.all()
    group = guyGroups.get(name=groupname)
    events = group.dinderevent_set.all()
    event = events.get(id=eventid)
    people = (event.dinderprofile_set.all())
    print(people)
    return HttpResponse("not implemented yet")
