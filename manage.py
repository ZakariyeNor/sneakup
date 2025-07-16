#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sneakup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



from products.models import Product
from cloudinary.uploader import upload

products = Product.objects.all()
for product in products:
    if product.image and not product.image.url.startswith('http'):
        result = upload(product.image.path, folder='products/product_images')
        product.image = result['public_id']  # Or CloudinaryField format
        product.save()
