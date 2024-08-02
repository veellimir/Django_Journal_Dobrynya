from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from news.models import News


@login_required
def home(request):
    news = News.objects.all().order_by('-created')

    context = {
        "title": "Главная",
        "news": news
    }
    return render(request, "mainapp/index.html", context)
