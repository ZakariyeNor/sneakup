from django.db import models
from datetime import date
from cloudinary.models import CloudinaryField


# Privacy policy model
class PrivacyPolicy(models.Model):
    """
    PrivacyPolicy model allowing the admin to dynamically manage
    the privacy policy content and upload a PDF version.
    """
    title = models.CharField(max_length=254, blank=False, null=False, default='Privacy Policy')
    content = models.TextField(help_text='The main text of the privacy policy')
    pdf = CloudinaryField(
        'file',
        resource_type='raw',
        folder='privacy_policies/', 
        blank=True, null=True,
        help_text="Upload a PDF version of the privacy policy (optional)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = 'Privacy Policies'

    def __str__(self):
        return f'Uploaded {self.title} on {self.updated_at.strftime("%Y-%m-%d")}'


# Returns policy model
class ReturnsPolicy(models.Model):
    """
    ReturnsPolicy model for managing the store's return policy content.

    This model allows an admin to upload a PDF version of the returns policy
    for users to download. It includes automatic timestamps for when the 
    policy was created and last updated.
    """
    title = models.CharField(max_length=254, blank=False, null=False, default='Returns Policy')
    pdf = CloudinaryField(
        'file',
        resource_type='raw',
        folder='returns_policies/', 
        blank=True, null=True,
        help_text="Upload a PDF version of the returns policy (optional)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = 'Returns Policies'

    def __str__(self):
        return f'Updated {self.title} on {self.updated_at.strftime("%Y-%m-%d")}'


# FAQs model
class FAQs(models.Model):
    """
    Frequently Asked Questions and their answers.
    """
    question = models.CharField(max_length=254, blank=False, null=False)
    answer = models.TextField(help_text="Provide a detailed answer to the question.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return f'FAQ: {self.id} | {self.created_at.strftime("%Y-%m-%d")}'


# Contact us form
class ContactMessage(models.Model):
    """
    Stores contact form submissions from users.
    """
    full_name = models.CharField(max_length=254, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    send_info = models.FileField(
        upload_to='contact_attachments/', blank=True, null=True,
    )
    order_number = models.CharField(
        max_length=100, blank=True, null=True,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'From: {self.full_name} | on {self.created_at.strftime("%Y-%m-%d")}'


# About page models
class AboutPageHero(models.Model):
    """
    Hero section with a background image and overlay text.
    """
    hero_image = CloudinaryField('image', folder='about/hero/', blank=False, null=False)
    overlay_title = models.CharField(max_length=254, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'About Page Hero'
        verbose_name = 'About Page Hero'
    def __str__(self):
        return self.overlay_title


# Our mission section
class OurMission(models.Model):
    """
    Our mission statement section.
    """
    our_mission_title = models.CharField(
        max_length=254, blank=False, null=False, default="Our Mission"
    )
    our_mission_description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.our_mission_title


# New arrivals section
class NewArrivals(models.Model):
    """
    New arrival product section.
    """
    class Meta:
        verbose_name_plural = 'New Arrivals'
    new_image = CloudinaryField('image', folder='about/new_images/', null=False, blank=False)
    new_name = models.CharField(max_length=100, blank=False, null=False)
    launched_date = models.DateField(blank=False, null=False)

    def date_since_launch(self):
        delta = (self.launched_date - date.today()).days
        return max(0, delta)

    def __str__(self):
        return f'{self.new_name} (Launch: {self.launched_date.strftime("%Y-%m-%d")})'


# Our Materials section
class OurMaterials(models.Model):
    """
    Our materials statement section.
    """
    class Meta:
        verbose_name_plural = 'Our Materials'

    our_materials_title = models.CharField(
        max_length=254, blank=False, null=False, default="Our Materials"
    )
    our_materials_description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.our_materials_title


# Best Seller section
class BestSelling(models.Model):
    """
    Best selling product section.
    """
    best_selling_title = models.CharField(
        max_length=254, blank=False, null=False,
    )
    best_image = CloudinaryField('image', folder='about/best_selling/', blank=False, null=False)
    best_description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.best_selling_title


# Launched Products section
class LaunchedProducts(models.Model):
    """
    Products launched in the last 3 years.
    """
    class Meta:
        verbose_name_plural = 'Launched Products'
    launched_image = CloudinaryField('image', folder='about/launched/', blank=False, null=False)
    launched_name = models.CharField(max_length=100, blank=False, null=False)
    launched_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return f'{self.launched_name} (Launch: {self.launched_date.strftime("%Y-%m-%d")})'
