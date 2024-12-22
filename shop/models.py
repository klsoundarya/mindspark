from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Mindspark Product Model"""

    CATEGORY_CHOICES = [
        (1, 'Montessori Essentials'),
        (2, 'Educational Toys'),
        (3, 'Teaching Tools'),
        (4, 'Arts & Crafts'),
        (5, 'Sensory Play'),
        (6, 'Board Games'),

    ]

    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    reviews_count = models.PositiveIntegerField(default=0)
    delivery = models.CharField(max_length=255, null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    age_group = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
