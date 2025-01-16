from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import BlogCategoryModel, BlogTagModel, BlogAuthorModel, BlogModel, BlogCommentModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'parent']
    search_fields = ['title']
    list_filter = ['parent']


@admin.register(BlogTagModel)
class BlogTagModelAdmin(MyTranslationAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(BlogAuthorModel)
class BlogAuthorModelAdmin(MyTranslationAdmin):
    list_display = ['first_name', 'last_name', 'avatar']
    search_fields = ['first_name', 'last_name']


@admin.register(BlogModel)
class BlogModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at', 'get_author_names']
    search_fields = ['title', 'description']
    filter_horizontal = ['author', 'categories']

    def get_author_names(self, obj):
        return ", ".join([author.get_full_name for author in obj.author.all()])

    get_author_names.short_description = 'Authors'


@admin.register(BlogCommentModel)
class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'created_at']
    search_fields = ['comment']
    list_filter = ['user']
