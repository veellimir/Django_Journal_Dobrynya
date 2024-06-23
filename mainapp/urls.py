from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("all-coach/", views.all_coach, name="all_coach"),
]