from django import template
from .. import services

register = template.Library()


@register.inclusion_tag(filename='women/post_categories_list.html', name='categories_show')
def show_categories(category_selected=0):
    categories = services.get_all_important_categories()
    return {'categories': categories, 'category_selected': category_selected}


@register.inclusion_tag(filename='women/post_tags_list.html')
def show_tags():
    return {'tags': services.get_all_important_tags()}
