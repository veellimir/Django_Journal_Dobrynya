from django.db import models

from mainapp.mixins import StrMixin


class News(StrMixin, models.Model):
    image_news = models.ImageField(upload_to="news_images/")
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Новостной заголовок")
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
