from django.contrib import admin
from Apps.Blog.models import Article, Portfolio
from django.core.cache import cache

# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = 'Mark selected articles as published.'

def make_draft(modeladmin, request, queryset):
    queryset.update(published=False)
make_draft.short_description = 'Mark selected articles as draft.'

class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ['title', 'published', 'pub_date']
    ordering = ['-pub_date']
    actions = [make_published, make_draft]
    exclude = ['author', 'slug']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user

        cache.delete('/'+obj.slug+'/')

        obj.save()

class PortfolioAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ['title', 'screenshot', 'pub_date']
    ordering = ['-pub_date']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Portfolio, PortfolioAdmin)