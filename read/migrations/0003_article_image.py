# Generated by Django 4.2 on 2025-02-15 00:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0002_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
