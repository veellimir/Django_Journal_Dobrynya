from django.db import models
from colorfield.fields import ColorField

from users.models import ProfileAdmin
from mainapp.mixins import StrMixin


class Event(StrMixin, models.Model):
    DAYS_OF_WEEK_CHOICES = (
        ("пн", 'Понедельник'),
        ("вт", 'Вторник'),
        ("ср", 'Среда'),
        ("чт", 'Четверг'),
        ("пт", 'Пятница'),
        ("сб", 'Суббота'),
        ("вс", 'Воскресенье'),
    )

    name = models.CharField(max_length=100, verbose_name="Направления тренировки")
    coaches = models.ManyToManyField(ProfileAdmin, blank=True, related_name="events", verbose_name="Тренер (ы)")
    title = models.CharField(max_length=200, verbose_name="Описания тренировки")

    start_time = models.TimeField(verbose_name="Начло в")
    end_time = models.TimeField(verbose_name="Конец в")

    days_of_week = models.CharField(max_length=50, blank=True, verbose_name="Дни недели на весь год")
    elem_color = ColorField(max_length=50, default="#0d6dfd7f", verbose_name="Цвет в расписании")

    class Meta:
        verbose_name = "тренировки"
        verbose_name_plural = "Тренировки"
