from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Woman, WomanCategory


def get_all_published_posts():
    return Woman.published.all()


def get_single_published_post_or_404(**kwargs):
    try:
        return get_object_or_404(Woman.published, **kwargs)
    except Woman.MultipleObjectsReturned:
        raise Http404()


def get_post_category_or_404(**kwargs):
    try:
        return get_object_or_404(WomanCategory, **kwargs)
    except WomanCategory.MultipleObjectsReturned:
        raise Http404()


def get_published_posts_by_category_id(category_id: int):
    return Woman.published.filter(category_id=category_id)