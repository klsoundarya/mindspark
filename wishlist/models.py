from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Wishlist(models.Model):
    """
    Wishlist model for users to keep track of their favourite products.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='wishlist',
                                     default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                null=False, blank=False,  default=None, related_name="wishlisted_by")
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name
