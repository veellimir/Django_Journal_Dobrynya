from django.db import models
from django.contrib.auth.models import User

from app.mainapp.base_mixins import StrMixin
from app.users.models import ProfileAdmin


class TaskUser(StrMixin, models.Model):
    NEW_TASK = 0
    WORK_TASK = 1
    CHECK_TASK = 2
    END_TASK = 3

    STATUSES_TASKS = (
        (NEW_TASK, "Новая"),
        (WORK_TASK, "В работе"),
        (CHECK_TASK, "На проверке"),
        (END_TASK, "Выполнено"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Выполняющий"
    )
    initiator = models.ForeignKey(
        ProfileAdmin,
        on_delete=models.CASCADE,
        related_name="initiated_tasks",
        verbose_name="Инициатор"
    )

    status_task = models.SmallIntegerField(
        default=NEW_TASK,
        choices=STATUSES_TASKS,
        verbose_name="Статус задачи",
    )

    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Названия задачи")
    description = models.TextField(blank=True, null=True, verbose_name="Описания")
    estimation_task = models.PositiveIntegerField(blank=True, null=True, verbose_name="Оценка")

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задачи"
