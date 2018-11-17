from django.http import HttpResponse

from .models import *

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