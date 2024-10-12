from datetime import datetime, timedelta
from typing import Optional

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from app_schedules.serializers import EventSerializer, CancelEventsSerializer
from attendance.serializers import AttendanceSerializer

from app_schedules.models import Event, CancelEvents
from attendance.models import UsersAttendance


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        year: Optional[str] = self.request.query_params.get("year")
        month: Optional[str] = self.request.query_params.get("month")

        if not year or not month:
            return UsersAttendance.objects.none()

        start_date = datetime(int(year), int(month), 1)
        end_date = (start_date.replace(day=28) + timedelta(days=4)).replace(day=1)
        return UsersAttendance.objects.filter(date__range=[start_date, end_date])


class CancelEventsListView(generics.ListAPIView):
    queryset = CancelEvents.objects.all()
    serializer_class = CancelEventsSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
