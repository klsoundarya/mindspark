# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    """Stores tags related to blog posts."""
    
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="blog_posts", blank=True)
    date = models.DateField("Post Date", default=date.today)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.title} | written by {self.author if self.author else 'Unknown'}"
