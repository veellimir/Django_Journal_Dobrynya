from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .models import News, LikeNews


@login_required
def home(request):
    news = News.objects.all().order_by('-created')
    user_likes = LikeNews.objects.filter(user=request.user).values_list("news_id", flat=True)

    for news_item in news:
        news_item.user_likes = LikeNews.objects.filter(news=news_item).select_related('user')

    context = {
        "title": "Главная",
        "news": news,
        "user_likes": user_likes,
    }
    return render(request, "news/index.html", context)


@login_required
def like_news(request, news_id):
    news_like = get_object_or_404(News, id=news_id)
    like, created = LikeNews.objects.get_or_create(user=request.user, news=news_like)

    if not created:
        like.delete()
    return redirect("home")