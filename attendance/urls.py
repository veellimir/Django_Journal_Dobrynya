from django.urls import path

from .views import TrainingDirectionsListView
from api.schedules import AttendanceListView


urlpatterns = [
    path("training-directions/", TrainingDirectionsListView.as_view(), name="training_directions_list"),

    path("api/attendance/", AttendanceListView.as_view(), name="attendance_list")
]
