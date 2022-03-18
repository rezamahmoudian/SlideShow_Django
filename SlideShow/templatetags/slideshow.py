from django import template
from ..models import Article


register = template.Library()

@register.inclusion_tag("../templates/slideshow.html")
def slideshow_tmptag():
    return {
        "articles": Article.objects.filter(status='p').order_by('-publish')
    }
