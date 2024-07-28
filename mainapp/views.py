from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from news.models import News
from .models import Coach


@login_required
def home(request):
    news = News.objects.all().order_by('-created')

    context = {
        "title": "Главная",
        "news": news
    }
    return render(request, "mainapp/index.html", context)


@login_required
def all_coach(request):
    coaches = Coach.objects.all()

    context = {
        "title": "Тренерский состав",
        "coaches": coaches,
    }
    return render(request, "mainapp/all_coach.html", context)