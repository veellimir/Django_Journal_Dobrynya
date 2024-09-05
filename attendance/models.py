from django.utils import timezone
from django.db import models

from users.models import Profile, TrainingDirections


class UsersAttendance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    direction = models.ForeignKey(TrainingDirections, on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ("profile", "direction", "date", )
