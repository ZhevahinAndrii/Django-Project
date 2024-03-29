from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Woman, WomanCategory, PostTag


def get_all_posts():
    return Woman.objects.all()


def get_all_published_posts():
    return Woman.published.all()


def get_all_categories():
    return WomanCategory.objects.all()


def get_all_tags():
    return PostTag.objects.all()


def get_all_important_categories():
    return (WomanCategory.objects.alias(posts_count=Count('post', filter=Q(post__status=Woman.Status.PUBLISHED))).
            filter(posts_count__gt=0))


def get_all_important_tags():
    return (PostTag.objects.alias(posts_count=Count('post', filter=Q(post__status=Woman.Status.PUBLISHED))).
            filter(posts_count__gt=0))


def get_single_published_post_with_tags_or_404(**kwargs) -> Woman:
    try:
        return get_object_or_404(Woman.published.prefetch_related('tags').defer('status', 'time_created', 'husband_id'),
                                 **kwargs)
    except Woman.MultipleObjectsReturned:
        raise Http404()


def get_post_category_or_404(**kwargs):
    try:
        return get_object_or_404(WomanCategory.objects.defer('slug'), **kwargs)
    except WomanCategory.MultipleObjectsReturned:
        raise Http404()


def get_post_tag_or_404(**kwargs):
    try:
        return get_object_or_404(PostTag.objects.defer('slug'), **kwargs)
    except PostTag.MultipleObjectsReturned:
        raise Http404()
