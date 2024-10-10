import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Count
from django.db.models import Value
from django.db.models.functions import Concat

from attendance.models import UsersAttendance


@method_decorator(login_required, name="dispatch")
class StatUsers(ListView):
    model = UsersAttendance
    template_name = "stats/all_stats.html"
    context_object_name = "stats_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Статистика"

        years = (
            UsersAttendance.objects
            .filter(is_present=True)
            .dates('date', 'year', order='DESC')
        )

        attendance_data = (
            UsersAttendance.objects
            .filter(is_present=True)
            .annotate(full_name=Concat(
                'profile__user__first_name',
                Value(' '),
                'profile__user__last_name')
            )
            .values('date__year', 'date__month', 'direction__name', 'full_name')
            .annotate(attendance_count=Count('id'))
            .order_by('date__year', 'date__month', 'direction__name')
        )

        attendance_by_year_and_month = {}
        for entry in attendance_data:
            year = entry['date__year']
            month = entry['date__month']
            direction = entry['direction__name']
            profile = entry['full_name']
            count = entry['attendance_count']

            if year not in attendance_by_year_and_month:
                attendance_by_year_and_month[year] = {}

            if month not in attendance_by_year_and_month[year]:
                attendance_by_year_and_month[year][month] = {}

            if direction not in attendance_by_year_and_month[year][month]:
                attendance_by_year_and_month[year][month][direction] = {}
            attendance_by_year_and_month[year][month][direction][profile] = count

        context['attendance_by_year_and_month_json'] = json.dumps(attendance_by_year_and_month)
        context['years'] = years
        return context
