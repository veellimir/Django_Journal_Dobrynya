from django.urls import path
from . import views
from . import api

urlpatterns = [
    path("schedules/", views.schedules, name="schedules"),

    path('api/events/', api.get_events, name='get_events'),
]