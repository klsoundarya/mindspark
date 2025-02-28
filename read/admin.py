from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

# Define custom admin configuration for Article model
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'published', 'created_at')
    list_filter = ('published',)
    search_fields = ('title', 'content')

# Register Article model with custom admin settings
admin.site.register(Article, ArticleAdmin)
