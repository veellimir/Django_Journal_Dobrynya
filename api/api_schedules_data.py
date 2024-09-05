from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app_schedules.models import Event

from api.serializers import EventSerializer


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

