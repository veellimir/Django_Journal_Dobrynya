from django.contrib import admin
from django.contrib.auth.models import User

from .models import ProfileAdmin


class UsersAdmin(admin.ModelAdmin):
    list_display =  (
        "username",
        "first_name",
        "last_name",
        "email",
    )

    list_display_links = ("username", "first_name", "last_name", "email")


admin.site.unregister(User)
admin.site.register(User, UsersAdmin)
admin.site.register(ProfileAdmin)
