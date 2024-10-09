from django.urls import path

from api import schedules
from . import views

urlpatterns = [
    path("schedules/", views.schedules, name="schedules"),

    path('api/events/', schedules.EventListView.as_view(), name='get_events'),
]