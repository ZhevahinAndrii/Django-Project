from django import template
from django.db.models import Count

import women_app.views as views
from women_app.models import WomanCategory
from ..services import get_all_important_tags, get_all_important_categories
register = template.Library()


@register.simple_tag(name='get_categories')
def get_categories():
    return views.categories


@register.inclusion_tag(filename='women/categories_list.html', name='categories_show')
def show_categories(category_selected=0):
    categories = get_all_important_categories()
    return {'categories': categories, 'category_selected': category_selected}


@register.inclusion_tag(filename='women/tags_list.html')
def show_tags():
    return {'tags': get_all_important_tags()}