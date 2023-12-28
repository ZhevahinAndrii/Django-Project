from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request: WSGIRequest):
    context = {
        'title': 'Index page',
    }
    return render(request, 'women/index.html', context=context, status=HTTPStatus.NO_CONTENT)


def archive(request: WSGIRequest, year1: int, year2: int):
    return HttpResponse(f'{year1}{year2}')
