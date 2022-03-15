from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
            ('p', "منتشر شده"),
            ('d', "پیش نویس"),
            ('i', "ارسال شده"),
            ('b', "برگشت داده شده"),
    )
    # author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده',
    #                            related_name='posts')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس')
    # category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name="posts")
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to="images", verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    special = models.BooleanField(default=False, verbose_name='مقاله ی ویژه')
    # views = models.ManyToManyField(IP_Address, through="ArticleViews", blank=True, related_name='views',
    #                                verbose_name="بازدید ها")
    # comments = GenericRelation(Comment)
    # for order by star rating
    # ratings = GenericRelation(Rating, related_query_name='rating')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title
