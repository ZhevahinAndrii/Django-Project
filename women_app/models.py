from django.db import models
from django.urls import reverse
from django.utils.text import gettext_lazy


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
    category = models.ForeignKey(to="WomanCategory", on_delete=models.SET_NULL, null=True,
                                 related_name="posts",
                                 related_query_name="post")
    tags = models.ManyToManyField(to='PostTag', blank=True, related_name='posts', related_query_name='post')
    husband = models.OneToOneField(to='Man', on_delete=models.SET_NULL, null=True, blank=True, related_name='wife')

    class Meta:
        verbose_name = gettext_lazy('Woman')
        verbose_name_plural = gettext_lazy('Women')
        constraints = (models.UniqueConstraint(fields=('slug',), name="woman_slug_unique_constraint"),)
        indexes = (models.Index(fields=('slug',)),)
        default_manager_name = 'published'
        base_manager_name = 'published'
        get_latest_by = 'time_created'

    def get_absolute_url(self):
        return reverse("women:post", kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class WomanCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)

    class Meta:
        constraints = (models.UniqueConstraint(fields=("slug",), name="cat_slug_unique_constraint"),)
        indexes = (models.Index(fields=('slug',)),)

    def get_absolute_url(self):
        return reverse("women:category", kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name


class PostTag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)

    class Meta:
        constraints = (models.UniqueConstraint(fields=("slug",), name="tag_slug_unique_constraint"),)
        indexes = (models.Index(fields=('slug',)),)

    def get_absolute_url(self):
        return reverse("women:tag", kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.title


class Man(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    marriages_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
