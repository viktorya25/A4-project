from django.db import models
from django.conf import settings


class Review(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")  # Связь с пользователем

    def __str__(self):
        return f"Отзыв от {self.author.username} ({self.created_at.strftime('%d.%m.%Y')})"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
