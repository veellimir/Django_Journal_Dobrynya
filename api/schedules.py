from datetime import datetime, timedelta
from typing import Optional

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.app_schedules.serializers import EventSerializer, CancelEventsSerializer
from app.attendance.serializers import AttendanceSerializer

from app.app_schedules.models import Event, CancelEvents
from app.attendance.models import UsersAttendance
from app.users.models import Profile


class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        profile = self._get_user_profile(user)
        filter_type = self.request.query_params.get("filter", "mine")

        if filter_type == "all":
            return Event.objects.filter(category="schedules_training")
        elif filter_type == "competition":
            return Event.objects.filter(category="competition")
        elif filter_type == "mine":
            if isinstance(profile, Profile):
                user_directions = profile.directions.all()
                return Event.objects.filter(name__in=user_directions, category="schedules_training").distinct()
            else:
                return Event.objects.filter(category="schedules_training")
        else:
            return Event.objects.none()

    def _get_user_profile(self, user):
        return (
                getattr(user, 'profile', None) or
                getattr(user, 'profileparent', None) or
                getattr(user, 'profileadmin', None)
        )


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
