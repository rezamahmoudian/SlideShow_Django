from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article
from django.utils.translation import activate, get_language_info
from django.http import HttpResponse
from django.utils.translation import gettext as _


# Create your views here.

# تغییر کلاس بیس ویوو به تابع برای اکتیو شدن زبان فارسی
def home(request):
    activate(request.GET.get('lang'))
    return render(request, 'home.html')

# class ArticleListView(ListView):
#     activate('fa')
#     template_name = 'home.html'
#     queryset = Article.objects.filter(status='p')
