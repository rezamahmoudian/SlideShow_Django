from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

# Create your views here.

from django.http import HttpResponse


class ArticleListView(ListView):
    template_name = 'slideshow.html'
    queryset = Article.objects.filter(status='p')
