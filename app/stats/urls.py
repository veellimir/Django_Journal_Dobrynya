from django.urls import path

from .views import StatUsers


urlpatterns = [
    path("stats-users/", StatUsers.as_view(), name="stats_users"),

]
