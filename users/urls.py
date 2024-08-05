from django.urls import path
from django.contrib.auth import views as auth_views

from users.forms import CustomSetPasswordForm

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("personal/", views.personal_data, name="personal"),

    path("reset_password/", auth_views.PasswordResetView.as_view(
        template_name="users/reset_password.html"),
         name="reset_password"
    ),
    path("reset_password_send/", auth_views.PasswordResetDoneView.as_view(
        template_name="users/reset_password_send.html"),
         name="password_reset_done"
    ),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="users/reset.html", form_class=CustomSetPasswordForm),
         name="password_reset_confirm",
    ),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="users/reset_password_compete.html"),
         name="password_reset_complete"
    ),

    path("questionnaire/", views.user_questionnaire, name="questionnaire"),
    path("all-users/", views.all_users, name="all_users"),
    path("all-coach/", views.all_coach, name="all_coach"),
    path("user/<int:pk>/", views.profile, name="profile"),
    path("edit-admin-profile/", views.edit_admin_profile, name="edit_admin_profile"),
]