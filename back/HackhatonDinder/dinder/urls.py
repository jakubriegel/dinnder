from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/login/<username>', views.loginView),
    path('api/login/<username>', views.logoutView),
    path('api/<uderid>/groups', views.showGroups),
    path('api/<userid>/groups/<groupname>', views.showEvents),
    path('api/<userid>/groups/<groupname>/events/<eventid>', views.showPeopleOfEvent),
]
