from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound


def page_not_found(request: WSGIRequest, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")