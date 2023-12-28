from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


menu = [{'title': 'About site', 'url_name': "women:about"}]
posts = [
    {'id': 1, 'title': 'Angelina Jolie', 'content': 'Angelina Jolie`s biography', 'is_published': True}
]
categories = [
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'}
]


def index(request: WSGIRequest):
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


def post(request: WSGIRequest, post_id: int):
    return HttpResponse(f"Showing post № {post_id}")


def show_category(request: WSGIRequest, category_id: int):
    context = {
        'title': 'Showing category',
        'menu': menu,
        'posts': posts,
        'category_selected': category_id
    }
    return render(request, 'women/index.html', context=context)
