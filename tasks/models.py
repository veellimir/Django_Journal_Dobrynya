from django.db import models

from django.contrib.auth.models import User


class TaskUser(models.Model):
    NEW_TASK = 0
    WORK_TASK = 1
    END_TASK = 2

    STATUSES_TASKS = (
        (NEW_TASK, "Новая"),
        (WORK_TASK, "В работе"),
        (END_TASK, "Выполнено"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Названия задачи")
    description = models.TextField(blank=True, null=True, verbose_name="Описания")
    status_task = models.SmallIntegerField(
        default=NEW_TASK,
        choices=STATUSES_TASKS,
        verbose_name="Статус задачи",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задачи"
