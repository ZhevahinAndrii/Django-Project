from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

import women_app.services as services
from .models import Woman

menu = [{'title': 'About site', 'url_name': "women:about"}]
categories = [
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'}
]


def index(request: WSGIRequest):
    posts = services.get_all_published_posts().select_related("category").defer('status', 'category__slug',
                                                                                'time_created', 'husband_id')
    context = {
        'title': 'Index page',
        'menu': menu,
        'posts': posts,
        'category_selected': 0
    }
    return render(request, 'women/index.html', context=context)


def about(request: WSGIRequest):
    context = {
        'title': 'About page',
        'menu': menu,
    }
    return render(request, 'women/about.html', context=context)


def show_post(request: WSGIRequest, post_slug: str):
    post_to_show: Woman = services.get_single_published_post_with_tags_or_404(slug=post_slug)
    data = {
        'title': post_to_show.title,
        'menu': menu,
        'post': post_to_show,
        'category_selected': post_to_show.category_id
    }
    return render(request, 'women/post.html', context=data)


def show_category(request: WSGIRequest, category_slug: str):
    category = services.get_post_category_or_404(slug=category_slug)
    posts = category.posts.defer('status', 'husband_id', 'time_created')
    context = {
        'title': f'Showing category: {category.name}',
        'menu': menu,
        'category_selected': category.pk,
        'posts': posts
    }
    return render(request, 'women/index.html', context=context)


def show_tag(request: WSGIRequest, tag_slug: str):
    tag = services.get_post_tag_or_404(slug=tag_slug)
    posts = tag.posts.select_related('category').defer('status', 'time_created', 'husband_id', 'category__slug')
    context = {
        'title': f'Tag: {tag.title}',
        'menu': menu,
        'posts': posts,
        'category_selected': None
    }
    return render(request, 'women/index.html', context=context)
