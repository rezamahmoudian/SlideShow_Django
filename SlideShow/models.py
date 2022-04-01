from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
            ('p', "منتشر شده"),
            ('d', "پیش نویس"),
    )
    title = TranslatedField(models.CharField(_('title'), max_length=200, default=0))
    slug = models.CharField(_('slug'), max_length=100, unique=True)
    content = models.TextField(_('content'))
    image = models.ImageField(_('image'), upload_to="images")
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(_('status'), max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def image_post(self):
        return format_html("<img width=150 height=160 border-radius: 5px; src='{}'>".format(self.image.url))

    image_post.short_description = _('image')