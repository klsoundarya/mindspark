from django import forms
from .models import Article

# Define form for creating and editing articles
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'external_link', 'image', 'published']
