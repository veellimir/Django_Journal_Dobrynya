from django.views.generic import ListView

from .models import UsersAttendance


class InfoAttendance(ListView):
    model = UsersAttendance
    template_name = "attendance/users_attendance.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Посещаемость"
        return context