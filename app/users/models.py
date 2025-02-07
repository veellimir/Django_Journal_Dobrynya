from django.db import models

from app.mainapp.base_mixins import StrMixin
from .mixins import SocialMixin


class TrainingDirections(StrMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Направление тренировки")

    class Meta:
        verbose_name = "направление тренировки"
        verbose_name_plural = "Направления тренировок"


class AdministrationPerson(StrMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Направление персонала")

    class Meta:
        verbose_name = "направление персонала"
        verbose_name_plural = "Направления персонала"


class Profile(SocialMixin, models.Model):
    directions = models.ManyToManyField(
        TrainingDirections,
        blank=False,
        verbose_name="Направления тренировок"
    )
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
        verbose_name="Домашний адрес"
    )

    fio_parents = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="ФИО и номер телефона родителей"
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
        verbose_name="Любимые виды спорта"
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
        verbose_name="Пожелания к тренировочному и организационному процессу в клубе"
    )
    points = models.PositiveIntegerField(
        default=3,
        verbose_name="Кол-во баллов профиля"
    )

    def __str__(self):
        return f"{self.user.get_full_name()} "

    class Meta:
        verbose_name = "дружинника"
        verbose_name_plural = "Вся дружина"


class ProfileParent(SocialMixin, models.Model):
    address = models.TextField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Домашний адрес"
    )
    parents_place_work = models.TextField(blank=True, null=True, verbose_name="Ваше место работы")
    children = models.ManyToManyField(
        "Profile",
        related_name="parents",
        verbose_name="Дети",
        blank=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} "

    class Meta:
        verbose_name = "Профиль родителя"
        verbose_name_plural = "Профиль родителей"


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
    directions = models.ManyToManyField(
        TrainingDirections,
        blank=True,
        verbose_name="Направления"
    )
    admin_personal = models.ManyToManyField(
        AdministrationPerson,
        blank=True,
        verbose_name="Направления персонала"
    )

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = "тренера"
        verbose_name_plural = "Тренерский состав"
