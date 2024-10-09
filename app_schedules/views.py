from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from typing import Dict


@login_required
def schedules(request: HttpRequest) -> HttpResponse:
    context: Dict[str, str] = {"title": "Календарь"}
    return render(request, "app_schedules/schedules.html", context)
