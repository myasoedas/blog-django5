from django.conf import settings
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(
        max_length=160,
        verbose_name="Заголовок страницы",
        help_text="Заголовок, отображаемый в браузере и поисковых системах"
    )
    slug = models.SlugField(
        max_length=160,
        verbose_name="URL-адрес (Slug)",
        unique=True,
        help_text="Уникальный идентификатор для URL-адреса страницы"
    )
    content_type = models.CharField(
        max_length=160,
        verbose_name="Тип контента",
        help_text="Тип или категория содержимого страницы (например, 'Статья' или 'Новость')"
    )
    og_image = models.URLField(
        max_length=250,
        verbose_name="URL изображения для Open Graph",
        help_text="Полный URL изображения, отображаемого при публикации ссылки в соцсетях"
    )
    og_image_alt = models.CharField(
        max_length=250,
        verbose_name="Описание изображения (alt-текст)",
        blank=True,
        help_text="Альтернативный текст для изображения (если требуется)"
    )
    description = models.CharField(
        max_length=160,
        verbose_name="Описание страницы (meta description)",
        help_text="Краткое описание для поисковых систем (не более 160 символов)"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    robots = models.CharField(
        max_length=500,
        verbose_name="Инструкции для поисковых систем (meta robots)",
        choices=[
            ("index, follow", "Индексировать и следовать"),
            ("noindex, follow", "Не индексировать, но следовать"),
            ("index, nofollow", "Индексировать, но не следовать"),
            ("noindex, nofollow", "Не индексировать и не следовать"),
        ],
        default="index, follow",
        help_text="Укажите, как поисковые системы должны обрабатывать страницу"
    )
    body = CKEditor5Field(config_name='default',
                          verbose_name="Текст публикации")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
            models.Index(fields=['slug']),
        ]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
