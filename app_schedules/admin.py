from django.contrib import admin

from .models import Event
from .forms import EventForm


class EventAdmin(admin.ModelAdmin):
    form = EventForm


admin.site.register(Event, EventAdmin)
