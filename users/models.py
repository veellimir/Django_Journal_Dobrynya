from django.db import models

from .mixins import SocialMixin


class Profile(SocialMixin, models.Model):
    date_of_birth = models.DateField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Дата рождения"
    )

    address = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Адрес"
    )

    fio_parents = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="ФИО родителей"
    )
    parents_place_work = models.TextField(blank=True, null=True, verbose_name="Место работы родителей")

    educational_institution = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Образовательное учреждение (школа, класс, ФИО классного руководителя, номер телефона)"
    )
    time_school = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Время начала и окончания учебных занятий в школе"
    )
    outside_club = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Дополнительные занятия вне клуба (кружки, секции); время"
    )
    hobby = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Хобби и увлечения"
    )
    sports = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Виды спорта больше всего нравятся ребёнку"
    )
    about_club = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Откуда узнали про клуб"
    )
    goals_season = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Цели на сезон"
    )
    PARTICIPATION_CHOICES = [
        ("yes", "Да"),
        ("no", "Нет")
    ]
    participation_competition = models.CharField(
        max_length=3,
        choices=PARTICIPATION_CHOICES,
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Участие в соревнованиях"
    )
    wishes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Пожелания"
    )


class ProfileAdmin(SocialMixin, models.Model):
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

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = "тренера"
        verbose_name_plural = "Тренерский состав"
