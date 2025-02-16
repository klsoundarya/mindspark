from django.db import models
from cloudinary.models import CloudinaryField

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title
