from django.contrib.auth.models import User
from django.db import models

from app.mainapp.base_mixins import StrMixin


class News(StrMixin, models.Model):
    image_news = models.ImageField(upload_to="news_images/")
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Новостной заголовок")
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)


    def total_like(self):
        return self.news_likes.count()


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class LikeNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_likes") # Переопределить удаление
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "news", )