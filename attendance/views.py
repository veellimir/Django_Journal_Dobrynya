from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView
from django.contrib import messages

from .models import TrainingDirections, UsersAttendance, Profile


@method_decorator(login_required, name="dispatch")
class TrainingDirectionsListView(ListView):
    model = TrainingDirections
    template_name = "attendance/users_attendance.html"
    context_object_name = "directions"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Журнал Посещаемости"

        selected_direction_id = self.request.GET.get("direction")
        if selected_direction_id:
            direction = get_object_or_404(TrainingDirections, pk=selected_direction_id)

            context["selected_direction"] = direction
            context["profiles"] = Profile.objects.filter(directions=direction)

            today = timezone.now().date()

            attendance_today = UsersAttendance.objects.filter(
                direction=direction,
                date=today
            ).exists()

            context["attendance_locked"] = attendance_today

            present_profiles = UsersAttendance.objects.filter(
                direction=direction,
                date=today,
                is_present=True
            ).values_list("profile__id", flat=True)
            context["present_profiles"] = present_profiles
        else:
            context["profiles"] = Profile.objects.none()
            context["present_profiles"] = []

        return context

    def post(self, request, *args, **kwargs):
        selected_direction_id = request.GET.get("direction")

        if not selected_direction_id:
            return redirect("training_directions_list")

        direction = get_object_or_404(TrainingDirections, pk=selected_direction_id)
        today = timezone.now().date()

        profiles = Profile.objects.filter(directions=direction)

        for profile in profiles:
            is_present = bool(request.POST.get(f"attendance_{profile.id}"))

            attendance, created = UsersAttendance.objects.get_or_create(
                profile=profile,
                direction=direction,
                date=today
            )
            attendance.is_present = is_present
            attendance.save()

        messages.success(request, "Отметки успешно обновлены")
        return redirect("training_directions_list")
