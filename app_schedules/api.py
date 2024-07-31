from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Event


@login_required
def get_events(request):
    events = Event.objects.all()
    events_list = [
        {
            "name": event.name,
            "title": event.title,
            "teacher": [
                {
                    "id": coach.id,
                    "name": coach.name,
                    "surname": coach.surname,
                    "patronymic": coach.patronymic
                }
                for coach in event.coaches.all()
            ],
            "start_time": event.start_time.strftime("%H:%M"),
            "end_time": event.end_time.strftime("%H:%M"),
            "days_of_week": event.days_of_week.split(","),
            "color_div": event.elem_color
        }
        for event in events
    ]
    return JsonResponse(events_list, safe=False)