from django.conf.urls import url
from django.urls import path,include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', views.EventView, basename='events')

urlpatterns = [
    path('', views.index, name='index'),
    url('api', include(router.urls)),
    # url('all-events', views.all_events)
]
