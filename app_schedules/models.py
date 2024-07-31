from django.db import models
from colorfield.fields import ColorField

from mainapp.models import Coach


class Event(models.Model):
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
    coaches = models.ManyToManyField(Coach, blank=True, related_name="events", verbose_name="Тренер (ы)")
    title = models.CharField(max_length=200, verbose_name="Описания тренировки")

    start_time = models.TimeField(verbose_name="Начло в")
    end_time = models.TimeField(verbose_name="Конец в")

    days_of_week = models.CharField(max_length=50, blank=True, verbose_name="Дни недели на весь год")
    elem_color = ColorField(max_length=50, default="#0d6dfd7f", verbose_name="Цвет в расписании")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тренировки"
        verbose_name_plural = "Тренировки"
