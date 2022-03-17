from django import template


register = template.Library()

@register.inclusion_tag("../templates/home.html")
def navbar_tmp_tag():
    return {
        "categorys": Category.objects.filter(status=True)
    }