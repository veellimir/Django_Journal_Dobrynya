from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def schedules(request):
    context = {'title': "Календарь"}

    return render(request, "app_schedules/schedules.html", context)
