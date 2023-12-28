from django import template


import women_app.views as views


register = template.Library()


@register.simple_tag(name='get_categories')
def get_categories():
    return views.categories


@register.inclusion_tag(filename='women/categories_list.html', name='categories_show')
def show_categories(category_selected=0):
    categories = views.categories
    return {'categories': categories, 'category_selected': category_selected}
