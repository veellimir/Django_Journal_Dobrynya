from typing import Dict

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.contrib import messages

from app.users.models import TrainingDirections
from app.app_schedules.models import CancelEvents
from app.news.utils import add_news


@login_required
def schedules(request: HttpRequest) -> HttpResponse:
    context: Dict[str, str] = {
        "title": "Календарь",
    }
    return render(request, "app_schedules/schedules.html", context)


@login_required
def cancel_training(request: HttpRequest):
    if request.method == "POST":
        cancelled_title: str = request.POST.get("cancelled_title")
        cancelled_date: str = request.POST.get("cancelled_date")
        description: str = request.POST.get("description")

        try:
            cancel_event = CancelEvents(
                cancelled_title=cancelled_title,
                cancelled_date=cancelled_date,
                description=description
            )
            cancel_event.save()
            add_news(cancelled_date, cancelled_title, description)

            messages.success(request, f"Тренировка отменена !")
            return redirect('schedules')
        except Exception as e:
            messages.error(request, f"Ошибка отмены тренировки")
            return HttpResponseBadRequest(f"Ошибка: {str(e)}")

    return render(request, "app_schedules/schedules.html", )