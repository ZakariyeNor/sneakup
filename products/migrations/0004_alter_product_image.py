# Generated by Django 5.2.3 on 2025-07-16 14:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_free_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default_image.jpg', max_length=255, verbose_name='Product image'),
            preserve_default=False,
        ),
    ]
