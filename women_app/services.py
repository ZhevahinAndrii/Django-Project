from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Woman


def get_all_published_posts():
    return Woman.published.all()


def get_single_woman_or_404(**kwargs):
    try:
        return get_object_or_404(Woman.published, **kwargs)
    except Woman.MultipleObjectsReturned:
        raise Http404()