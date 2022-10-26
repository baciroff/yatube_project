from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.TextField(
        max_length=50,
        verbose_name='Сообщество')
    slug  = models.SlugField(
        unique=True,
        verbose_name='URL адрес группы')
    description = models.TextField(
        verbose_name='Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='posts',
        verbose_name='Автор')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Сообщество')
