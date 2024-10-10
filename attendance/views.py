from typing import Dict, List, Optional

from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpRequest, HttpResponse

from .models import TrainingDirections, UsersAttendance, Profile


@method_decorator(login_required, name="dispatch")
class TrainingDirectionsListView(ListView):
    model = TrainingDirections
    template_name = "attendance/users_attendance.html"
    context_object_name = "directions"

    def get_context_data(
            self, *,
            object_list: Optional[List[TrainingDirections]] = None,
            **kwargs: Dict[str, any]
    ) -> Dict[str, any]:
        context: Dict[str, any] = super().get_context_data(**kwargs)
        context["title"] = "Журнал Посещаемости"

        selected_direction_id: Optional[str] = self.request.GET.get("direction")
        selected_date: Optional[str] = self.request.GET.get("date")

        if not selected_date:
            today = timezone.now().date()
        else:
            try:
                today = timezone.datetime.strptime(selected_date, "%Y-%m-%d").date()
            except ValueError:
                today = timezone.now().date()
        context["selected_date"] = today

        if selected_direction_id:
            direction = get_object_or_404(TrainingDirections, pk=selected_direction_id)
            context["selected_direction"] = direction
            context["profiles"] = Profile.objects.filter(directions=direction)

            attendance_today: bool = UsersAttendance.objects.filter(
                direction=direction,
                date=today
            ).exists()

            context["attendance_locked"] = attendance_today

            present_profiles: List[int] = UsersAttendance.objects.filter(
                direction=direction,
                date=today,
                is_present=True
            ).values_list("profile__id", flat=True)
            context["present_profiles"] = present_profiles
        else:
            context["profiles"] = Profile.objects.none()
            context["present_profiles"] = []
        return context

    def post(self, request: HttpRequest, *args: any, **kwargs: any) -> HttpResponse:
        selected_direction_id: Optional[str] = request.GET.get("direction")
        selected_date: Optional[str] = request.POST.get("date")

        if not selected_date:
            today = timezone.now().date()
        else:
            try:
                today = timezone.datetime.strptime(selected_date, "%Y-%m-%d").date()
            except ValueError:
                today = timezone.now().date()

        if not selected_direction_id:
            return redirect("training_directions_list")

        direction: TrainingDirections = get_object_or_404(TrainingDirections, pk=selected_direction_id)
        profiles: List[Profile] = Profile.objects.filter(directions=direction)

        for profile in profiles:
            is_present = bool(request.POST.get(f"attendance_{profile.id}"))

            attendance, created = UsersAttendance.objects.get_or_create(
                profile=profile,
                direction=direction,
                date=today
            )
            if is_present and (created or not attendance.is_present):
                profile.points += 2
                profile.save()

            attendance.is_present = is_present
            attendance.save()

        messages.success(request, "Отметки успешно обновлены")
        return redirect("training_directions_list")
