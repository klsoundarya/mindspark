from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Product
from wishlist.models import Wishlist


class WishlistModelTest(TestCase):
    def setUp(self):
        """Set up test user and product before each test"""
        self.user = User.objects.create_user(
                username="testuser", password="testpassword")
        self.product = Product.objects.create(name="Test Product", price=10.99)

    def test_wishlist_entry_creation(self):
        """Test that a Wishlist entry is created correctly"""
        wishlist_item = Wishlist.objects.create(
                user=self.user, product=self.product)
        self.assertEqual(Wishlist.objects.count(), 1)
        self.assertEqual(wishlist_item.user, self.user)
        self.assertEqual(wishlist_item.product, self.product)
        self.assertTrue(wishlist_item.added_at)

    def test_wishlist_str_method(self):
        """Test the string representation of the Wishlist model"""
        wishlist_item = Wishlist.objects.create(
                user=self.user, product=self.product)
        self.assertEqual(str(wishlist_item), f"testuser - {self.product.name}")

    def test_wishlist_deletes_on_user_delete(self):
        """Test that deleting a user removes their wishlist items"""
        Wishlist.objects.create(user=self.user, product=self.product)
        self.user.delete()
        self.assertEqual(Wishlist.objects.count(), 0)

    def test_wishlist_deletes_on_product_delete(self):
        """Test that deleting a product removes associated wishlist items"""
        Wishlist.objects.create(user=self.user, product=self.product)
        self.product.delete()
        self.assertEqual(Wishlist.objects.count(), 0)
