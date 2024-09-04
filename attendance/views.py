from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from users.models import Profile, TrainingDirections


@method_decorator(login_required, name='dispatch')
class TrainingDirectionsListView(ListView):
    model = TrainingDirections
    template_name = "attendance/users_attendance.html"
    context_object_name = "directions"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Журнал Посещаемости"

        selected_direction_id = self.request.GET.get('direction')
        if selected_direction_id:
            direction = get_object_or_404(TrainingDirections, pk=selected_direction_id)
            context['selected_direction'] = direction
            context['profiles'] = Profile.objects.filter(directions=direction)
        else:
            context['profiles'] = Profile.objects.none()
        return context