from django.contrib import admin

from .models import Coach

admin.site.register(Coach)

admin.site.site_title = "Админ-панель Клуба Добрыня"
admin.site.site_header = "Админ-панель Клуба Добрыня"
