from django.contrib import admin
from django.contrib.auth.models import User

from app.app_schedules.models import Event
from app.app_schedules.forms import EventForm
from app.tasks.models import TaskUser
from app.users.models import ProfileAdmin, Profile, ProfileParent, TrainingDirections
from app.news.models import News


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )

    list_display_links = ("username", "first_name", "last_name", "email", )


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    filter_horizontal = ("coaches", )



admin.site.unregister(User)

admin.site.register(User, UsersAdmin)
admin.site.register(Profile)
admin.site.register(ProfileParent)
admin.site.register(ProfileAdmin)
admin.site.register(TrainingDirections)

admin.site.register(Event, EventAdmin)

admin.site.register(TaskUser)

admin.site.register(News)

admin.site.site_title = "Админ-панель Клуба Добрыня"
admin.site.site_header = "Админ-панель Клуба Добрыня"