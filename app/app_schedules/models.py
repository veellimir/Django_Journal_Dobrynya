from django.db import models
from django.core.exceptions import ValidationError

from colorfield.fields import ColorField

from app.mainapp.base_mixins import StrMixin
from app.users.models import ProfileAdmin, TrainingDirections


class Event(StrMixin, models.Model):
    EVENT_TYPE_CHOICES = (
        ("schedules_training", "Расписания",),
        ("competition", "Мероприятие",),
    )
    DAYS_OF_WEEK_CHOICES = (
        ("пн", 'Понедельник'),
        ("вт", 'Вторник'),
        ("ср", 'Среда'),
        ("чт", 'Четверг'),
        ("пт", 'Пятница'),
        ("сб", 'Суббота'),
        ("вс", 'Воскресенье'),
    )
    name = models.OneToOneField(
        TrainingDirections,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Направление"
    )
    competition_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Название мероприятия"
    )
    coaches = models.ManyToManyField(ProfileAdmin, blank=True, related_name="events", verbose_name="Тренер (ы)")
    title = models.CharField(max_length=200, verbose_name="Описание тренировки")
    start_time = models.TimeField(verbose_name="Начло в")
    end_time = models.TimeField(verbose_name="Конец в")
    days_of_week = models.CharField(max_length=50, blank=True, verbose_name="Дни недели на весь год")
    elem_color = ColorField(max_length=50, default="#0d6dfd7f", verbose_name="Цвет в расписании")
    category = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
        default="schedules_training",
        verbose_name="Тип события",
        blank=False,
        null=False
    )
    event_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата мероприятия (Указывать если выбран тип - Мероприятие)"
    )

    class Meta:
        verbose_name = "тренировку или событие"
        verbose_name_plural = "Тренировки и события"

    def save(self, *args: tuple, **kwargs: dict) -> None:
        if self.category == "competition" and not self.event_date:
            raise ValueError("Для мероприятия необходимо указать дату.")
        elif self.category == "schedules_training" and not self.days_of_week:
            raise ValueError("Для тренировки необходимо указать дни недели.")
        super().save(*args, **kwargs)

    def clean(self):
        if self.category == 'competition':
            if not self.competition_name:
                raise ValidationError("Поле 'Название мероприятия' обязательно для события типа 'Мероприятие'.")
            self.name = None
        else:
            if self.competition_name:
                raise ValidationError(
                    "Поле 'Название мероприятия' не должно быть заполнено для события типа 'Расписание'.")
            self.competition_name = None

        if self.category == 'schedules_training' and not self.name:
            raise ValidationError("Поле 'Направление' обязательно для события типа 'Расписание'.")


class CancelEvents(models.Model):
    cancelled_title = models.CharField(max_length=100, verbose_name="Название тренировки")
    cancelled_date = models.DateTimeField(verbose_name="Дата отмены")
    cancelled_red_color = models.CharField(max_length=7, default="#FF0000")
    description = models.TextField(blank=True, null=True, verbose_name="Описание отмены")
