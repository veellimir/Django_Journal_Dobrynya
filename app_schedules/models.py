from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
