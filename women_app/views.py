from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import women_app.services as services
from women_app.models import Woman


menu = [{'title': 'About site', 'url_name': "women:about"}]
categories = [
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'}
]


def index(request: WSGIRequest):
    posts = services.get_all_published_posts()
    context = {
        'title': 'Index page',
        'menu': menu,
        'posts': posts
    }
    return render(request, 'women/index.html', context=context)


def about(request: WSGIRequest):
    context = {
        'title': 'About page',
        'menu': menu
    }
    return render(request, 'women/about.html', context=context)


def post(request: WSGIRequest, post_slug: str):
    post_to_show: Woman = services.get_single_woman_or_404(slug=post_slug)
    data = {
        'title': post_to_show.title,
        'menu': menu,
        'post': post_to_show,
        'cat_selected': 0
    }
    return render(request, 'women/post.html', context=data)


def show_category(request: WSGIRequest, category_id: int):
    context = {
        'title': 'Showing category',
        'menu': menu,
        'category_selected': category_id
    }
    return render(request, 'women/index.html', context=context)
