from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag('furniture/navbar_catalog.html', takes_context=True)
def navbar_catalog(context):
    context['categories'] = Category.objects.all()
    return context


@register.inclusion_tag('furniture/furniture_list.html')
def furniture_list(furniture, page_obj):
    return {'furniture': furniture, 'page_obj': page_obj}
