from datetime import datetime, timedelta
from typing import Optional

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.app_schedules.serializers import EventSerializer, CancelEventsSerializer
from app.attendance.serializers import AttendanceSerializer

from app.app_schedules.models import Event, CancelEvents
from app.attendance.models import UsersAttendance


class EventListView(generics.ListAPIView):
    # queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    # TODO: по умолчанию тренировки только пользователя
    # def get_queryset(self):
    #     user = self.request.user
    #     profile = user.profile
    #     user_directions = profile.directions.all()
    #
    #     filter_type = self.request.query_params.get('filter', 'mine')  # Если параметр не указан, фильтруем по умолчанию (mine)
    #     if filter_type == 'mine':  # Фильтровать только события текущего пользователя
    #         return Event.objects.filter(name__in=user_directions).distinct()
    #     elif filter_type == 'all':  # Отображать все события
    #         return Event.objects.all()
    #     else:
    #         # Если передан неправильный параметр фильтрации, возвращаем пустой набор
    #         return Event.objects.none()
    def get_queryset(self):
        user = self.request.user
        profile = user.profile

        # Проверяем, есть ли параметр "all" в запросе
        filter_type = self.request.query_params.get('filter', 'mine')  # mine по умолчанию
        all_param = self.request.query_params.get('all', 'false') == 'true'

        if filter_type == 'all' or all_param:
            # Возвращаем все события
            return Event.objects.all()
        elif filter_type == 'competition':
            # Возвращаем только мероприятия
            return Event.objects.filter(category="мероприятие").distinct()
        else:
            # Возвращаем события пользователя
            user_directions = profile.directions.all()
            return Event.objects.filter(name__in=user_directions).distinct()


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

