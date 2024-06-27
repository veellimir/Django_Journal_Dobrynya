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
            "start_time": event.start_time.strftime("%H:%M"),
            "end_time": event.end_time.strftime("%H:%M"),
            "description": event.description,
            "days_of_week": event.days_of_week.split(",")
        }
        for event in events
    ]
    return JsonResponse(events_list, safe=False)