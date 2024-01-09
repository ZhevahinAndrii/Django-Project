from django.contrib import admin


from .models import Woman, WomanCategory


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'time_last_modified', 'status')
    list_display_links = ('id', 'title')
    list_editable = ('status',)
    ordering = ('time_created', )


@admin.register(WomanCategory)
class WomanCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)




