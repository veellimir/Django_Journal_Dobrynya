from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Event


@login_required
def schedules(request):
    events = Event.objects.all()

    context = {
        'events': events
    }
    return render(request, "app_schedules/schedules.html", context)
