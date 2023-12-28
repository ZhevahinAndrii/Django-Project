from django.db import models
from django.utils.text import gettext_lazy


class Woman(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, gettext_lazy("Not published")
        PUBLISHED = 1, gettext_lazy("Published")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices)

    class Meta:
        verbose_name = gettext_lazy('Woman ')
        verbose_name_plural = gettext_lazy('Women ')
