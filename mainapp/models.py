from django.db import models


class Coach(models.Model):
    img_coach = models.ImageField(
        upload_to="coach_images/",
        blank=False, null=False,
        verbose_name="Изображения тренера"
    )
    name = models.CharField(
        max_length=20, blank=False, null=False,
        verbose_name="Имя тренера"
    )
    surname = models.CharField(
        max_length=20, blank=False, null=False,
        verbose_name="Фамилия тренера"
    )
    patronymic = models.CharField(
        max_length=20, blank=False, null=False,
        verbose_name="Отчество тренера"
    )
    directions = models.CharField(
        max_length=50, blank=False, null=False,
        verbose_name="Направления"
    )
    phone = models.CharField(
        max_length=20, blank=False, null=False,
        verbose_name="Номер телефона"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тренера"
        verbose_name_plural = "Тренерский состав"

