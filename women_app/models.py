from django.db import models
from django.db.models import F
from django.utils.text import gettext_lazy
from django.urls import reverse


class PublishedPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Woman.Status.PUBLISHED)


class Woman(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, gettext_lazy("Not published")
        PUBLISHED = 1, gettext_lazy("Published")
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.PUBLISHED)
    objects = models.Manager()
    published = PublishedPostsManager()

    class Meta:
        verbose_name = gettext_lazy('Woman')
        verbose_name_plural = gettext_lazy('Women')
        constraints = (models.UniqueConstraint(fields=('slug',), name="slug_unique_constraint"),)
        indexes = (models.Index(fields=('slug',)),)

    def get_absolute_url(self):
        return reverse("women:post", kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title
