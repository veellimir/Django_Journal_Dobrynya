from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("app.users.urls")),
    path("", include("app.app_schedules.urls")),
    path("", include("app.tasks.urls")),
    path("", include("app.news.urls")),
    path("", include("app.attendance.urls")),
    path("", include("app.stats.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

