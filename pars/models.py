from django.db import models
from django.db.models.fields import URLField
class Information(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField('Заголовок', max_length=150)
    teg = models.CharField('Теги', max_length=150)
    body = models.CharField('Описание', max_length=150)
    user = models.CharField('Пользователь', max_length=150)
    info = models.CharField('Информация', max_length=150)
    
    hab = models.CharField('Хабы', max_length=150)
    time = models.CharField('Время', max_length=150)
    image =models.CharField('Кратинка', max_length=150)
    vote = models.CharField('Голосы', max_length=150)
    bookmarks = models.CharField('Избранные', max_length=150)
    contact = models.CharField('Контакт', max_length=150)
    user_content_karma = models.CharField('Карма Пользователя', max_length=150)
    user_content_rate = models.CharField('Рейтинг Пользователя', max_length=150)
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
class Follower(models.Model):
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.email
# Create your models here.
