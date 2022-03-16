from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.site_header = "صفحه ی مدیریت"

class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'image_post', 'slug',  'status')
    list_filter = ('publish', 'status')
    ordering = ('-status', '-publish')
    search_fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Article, AdminArticle)