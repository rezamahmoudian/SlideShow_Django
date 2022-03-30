from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from translated_fields import TranslatedField
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
            ('p', "منتشر شده"),
            ('d', "پیش نویس"),
    )
    title = TranslatedField(models.CharField(max_length=200, verbose_name='عنوان', default=0))
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to="images", verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def image_post(self):
        return format_html("<img width=150 height=160 border-radius: 5px; src='{}'>".format(self.image.url))
