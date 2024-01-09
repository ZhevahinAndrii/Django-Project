from django.contrib import admin, messages
from django.db.models import QuerySet

from .models import Woman, WomanCategory


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус жінки'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return[
            ('married', 'Заміжня'),
            ('single', 'Незаміжня')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)
        else:
            return queryset


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'slug', 'category')
    list_display = ('title', 'time_created', 'time_last_modified', 'status', 'category', 'brief_info')
    list_display_links = ('title',)
    list_editable = ('status', 'category')
    ordering = ('time_created',)
    list_per_page = 3
    actions = ('set_published', 'set_draft')
    search_fields = ('title', 'category__name')
    list_filter = (MarriedFilter, 'category__name', 'status')
    show_facets = False


    @staticmethod
    @admin.display(description='Короткий опис', ordering='content')
    def brief_info(woman: Woman):
        return f"Опис {len(woman.content)} символів"

    @admin.action(description='Опублікувати обрані публікації')
    def set_published(self, request, queryset: QuerySet[Woman]):
        count = queryset.update(status=Woman.Status.PUBLISHED)
        self.message_user(request, f'Опубліковано {count} публікації')

    @admin.action(description='Зняти з публікації')
    def set_draft(self, request, queryset: QuerySet[Woman]):
        count = queryset.update(status=Woman.Status.DRAFT)
        self.message_user(request, f'Зняті {count} публікації', messages.WARNING)

    def get_queryset(self, request):
        return Woman.objects.all().select_related('category')

@admin.register(WomanCategory)
class WomanCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)
