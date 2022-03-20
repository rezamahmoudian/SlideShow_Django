from django.urls import path

# from .views import ArticleListView
from .views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', ArticleListView.as_view(), name='index'),
    path('', home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

