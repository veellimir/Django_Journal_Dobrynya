from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("news/<int:news_id>/like/", views.like_news, name="like_news")
]