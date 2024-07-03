from django.contrib import admin

from .models import Event
from .forms import EventForm


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    filter_horizontal = ("coaches", )


admin.site.register(Event, EventAdmin)
