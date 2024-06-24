from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from users.forms import CustomSetPasswordForm


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("mainapp.urls")),
    path("", include("users.urls")),
    path("", include("app_schedules.urls")),


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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
