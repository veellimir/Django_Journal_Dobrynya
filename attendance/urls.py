from django.urls import path

from .views import *

urlpatterns = [
    path("attendance/", InfoAttendance.as_view(), name="users_attendance"),


]