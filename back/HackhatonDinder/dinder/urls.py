from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/login/<username>', views.loginView),
    path('api/login/<username>', views.logoutView),
    path('api/<userid>/groups', views.showGroups),
    path('api/<userid>/groups/<groupid>', views.showEvents),
    path('api/<userid>/groups/<groupid>/events/<eventid>', views.showPeopleOfEvent),
    path('api/<userid>/nearby/<lat>/<lng>', views.get_nearby),
    path('api/<userid>/create/group', views.groupMaker),
    path('api/<userid>/<groupid>/create/event', views.eventMaker),
]
