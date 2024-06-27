from django.db import models


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
    title = models.CharField(max_length=200, verbose_name="Описания тренировки")

    start_time = models.TimeField(verbose_name="Начло в")
    end_time = models.TimeField(verbose_name="Конец в")
    description = models.TextField(blank=True, null=True)

    days_of_week = models.CharField(max_length=50, blank=True, help_text="Дни недели на весь год")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тренировки"
        verbose_name_plural = "Тренировки"
