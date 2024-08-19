from django.urls import path

from api import get
from . import views

urlpatterns = [
    path("schedules/", views.schedules, name="schedules"),

    path('api/events/', get.get_events, name='get_events'),
]