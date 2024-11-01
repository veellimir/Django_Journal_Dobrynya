from django.urls import path

from api import schedules
from . import views

urlpatterns = [
    path("schedules/", views.schedules, name="schedules"),

    path('api/events/', schedules.EventListView.as_view(), name='get_events'),
    path('cancel-event/', views.cancel_training, name='cancel_event'),
    path('api/cancel-event/', schedules.CancelEventsListView.as_view(), name='get_cancel_event'),
]