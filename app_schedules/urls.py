from django.urls import path

from api import api_data
from . import views

urlpatterns = [
    path("schedules/", views.schedules, name="schedules"),

    path('api/events/', api_data.EventListView.as_view(), name='get_events'),
]