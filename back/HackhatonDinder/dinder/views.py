from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dinder import models, serializers
from dinder.models import DinderEvent
from dinder.serializers import EventSerializer


class EventView(viewsets.ModelViewSet):
    # queryset = DinderEvent.objects.all()
    # serializer_class = serializers.EventSerializer

    def list(self, request, *args, **kwargs):
        print("list --- list")
        queryset = DinderEvent.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        print("ret --- ret")
        return super().retrieve(request, *args, **kwargs)

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)


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
