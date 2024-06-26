from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),

    path("questionnaire/", views.user_questionnaire, name="questionnaire"),
    path("all-users/", views.all_users, name="all_users"),
    path("user/<int:pk>/", views.profile, name="profile"),
]