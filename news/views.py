from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import News


@login_required
def home(request):
    news = News.objects.all().order_by('-created')

    context = {
        "title": "Главная",
        "news": news
    }
    return render(request, "news/index.html", context)