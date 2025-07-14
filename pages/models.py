from django.db import models
from datetime import date

# Privacy policy model
class PrivacyPolicy(models.Model):
    """
    PrivacyPolicy model allowing the admin to dynamically manage
    the privacy policy content and upload a PDF version.
    """
    title = models.CharField(max_length=254, blank=False, null=False, default='Privacy Policy')
    content = models.TextField(help_text='The main text of the privacy policy')
    pdf = models.FileField(
        upload_to='privacy_policies/', blank=True, null=True,
        help_text="Upload a PDF version of the privacy policy (optional)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

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
    pdf = models.FileField(
        upload_to='returns_policies/', blank=True, null=True,
        help_text="Upload a PDF version of the returns policy (optional)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

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
    hero_image = models.ImageField(upload_to='about/hero/', blank=False, null=False)
    overlay_title = models.CharField(max_length=254, blank=False, null=False)

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
        return self.our_mission_title  # Fixed: use correct field name

# New arrivals section
class NewArrivals(models.Model):
    """
    New arrival product section.
    """
    new_title = models.CharField(
        max_length=254, blank=False, null=False, default="New Arrivals"
    )
    new_image = models.ImageField(upload_to='about/new_arrivals/', blank=False, null=False)
    new_name = models.CharField(max_length=100, blank=False, null=False)
    launched_date = models.DateField(blank=False, null=False)

    def date_since_launch(self):
        # Fixed typo: self.date.today() → date.today()
        delta = (self.launched_date - date.today()).days
        return max(0, delta)

    def __str__(self):
        return f'{self.new_name} (Launch: {self.launched_date.strftime("%Y-%m-%d")})'