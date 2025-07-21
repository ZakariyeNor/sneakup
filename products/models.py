from django.db import models
from cloudinary.models import CloudinaryField


# Category model
class Category(models.Model):
    """
    Represents a product category.

    Categories are used to organize products into groups.
    Admins can create new categories or assign existing ones
    when adding new products.
    """
    # Customize the categories admin
    class Meta:
        verbose_name_plural = 'Categories'

    # Requirement field for a new category
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def display_friendly_name(self):
        return self.friendly_name


# Products model
class Product(models.Model):
    """
    Represents a single product in the store.

    This model stores all relevant product data such as
    name, SKU, price, description, image, and size. It is
    linked to the Category model to classify each product
    under a specific category.
    """
    # Basic fields
    name = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()

    # Filter fields p-1
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    # Product that has sizes
    size = models.JSONField(null=True, blank=True)
    # For products that has no sizes
    free_size = models.BooleanField(default=False)

    # Filter fields p-2
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    # Image fields
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField(
        'image', folder='product_images/', null=True, blank=True)

    def size_list(self):
        return self.size.split(',') if self.size else []

    def __str__(self):
        return self.name
