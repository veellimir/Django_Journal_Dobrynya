from django.db import models

from django.contrib.auth.models import User


class SocialMixin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True, null=True,
        verbose_name="Изображения профиля"
    )
    phone = models.CharField(max_length=110, blank=True, null=True, verbose_name="Номер телефона")
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Телеграм")
    vk = models.CharField(max_length=100, blank=True, null=True, verbose_name="Вконтакте")

    class Meta:
        abstract = True
