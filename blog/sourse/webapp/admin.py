from django.contrib import admin

from webapp.models import Article  # импортируем модель

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'cotegory', 'created_at']
    list_filter = ['author', 'cotegory']
    search_fields = ['title', 'text']
    fields = ['title', 'author', 'text',  'created_at', 'updated_at', 'cotegory']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)
