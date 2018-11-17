from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import *
import json
from rest_framework.decorators import api_view
def index(request):
    return HttpResponse("Dinder home.")


def loginView(request, username):

    print('not implemented login')

    return HttpResponse("not implemented login")


def logoutView(request, username):
    print('not implemented logout')

    return HttpResponse("not implemented logout")

def showGroups(request,userid):
    guy = DinderProfile.objects.get(id=userid)
    guyGroups = guy.groups.all()
    #object with groups of guy
    pass

def showEvents(request,userid,groupname):
    guy = DinderProfile.objects.get(id=userid)
    guyGroups = guy.groups.all()
    group = guyGroups.get(name=groupname)
    events = group.dinderevent_set.all()
    #objects with events of a guy's chosen group

def showPeopleOfEvent(request,userid,groupname,eventid):
    guy = DinderProfile.objects.get(id=userid)
    guyGroups = guy.groups.all()
    group = guyGroups.get(name=groupname)
    events = group.dinderevent_set.all()
    event = events.get(id=eventid)
    people = (event.dinderprofile_set.all())
    print(people)
    return HttpResponse("not implemented yet")


# @api_view(['POST'])
# @csrf_exempt
# def createGroup(request):
#         data = json.loads(request.body.decode("utf-8"))
#         #group = DinderGroup(name=data['userid'])
#         print(data)
#         return HttpResponse("XD")


@api_view(['POST'])
@csrf_exempt
def makegroup(request):
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    return HttpResponse("not implemented yet")


@api_view(['POST'])
@csrf_exempt
def groupMaker(request,userid):
    data = json.loads(request.body.decode("utf-8"))
    group = DinderGroup(name=data['groupname'])
    group.save()
    guy = DinderProfile.objects.get(id=int(userid))
    guy.groups.add(group)

    return HttpResponse("not implemented yet")

@api_view(['POST'])
@csrf_exempt
def eventMaker(request,userid,groupid):
    data = json.loads(request.body.decode("utf-8"))
    guy = DinderProfile.objects.get(id=int(userid))
    groupofguy = DinderGroup.objects.get(id=int(groupid))
    event = DinderEvent(name=data['eventname'],group=groupofguy)
    event.save()
    guy.events.add(event)

    return HttpResponse("not implemented yet")