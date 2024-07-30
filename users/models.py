from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True, null=True,
        verbose_name="Изображения профиля"
    )

    date_of_birth = models.DateField(
        blank=False,
        null=False,
        help_text="*",
        verbose_name="Дата рождения"
    )

    phone = models.CharField(max_length=110, blank=True, null=True, verbose_name="Номер телефона")
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Телеграм")
    vk = models.CharField(max_length=100, blank=True, null=True, verbose_name="Вконтакте")
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
