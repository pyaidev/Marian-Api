from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ['title', ]
    list_display_links = ('title', 'id')
    list_per_page = 50
    search_help_text = 'search on here'


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title', ]
    list_filter = ('id', 'title')
    list_display_links = ('title', 'id')
    search_help_text = 'search on here'


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category')
    search_fields = ['title', 'author__username', 'category__title']
    list_filter = ('category', 'tags')
    list_display_links = ('title', 'id', 'author')
    filter_horizontal = ('tags', )
    search_help_text = 'search on here'
    date_hierarchy = 'created_at'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
