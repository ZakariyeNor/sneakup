from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


# User profile model
class Profile(models.Model):
    """
    A User profile model for default delivery
    information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
                        max_length=20, blank=True, null=True)
    default_street_address_1 = models.CharField(
                                max_length=80, blank=True, null=True)
    default_street_address_2 = models.CharField(
                                max_length=80, blank=True, null=True)
    default_city = models.CharField(max_length=40, blank=True, null=True)
    default_postcode = models.CharField(max_length=20, blank=True, null=True)
    default_county = models.CharField(max_length=70, blank=True, null=True)
    default_country = CountryField(
                    blank_label="Country", blank=True, null=True)

    def __str__(self):
        return self.user.username


# Signals
@receiver(post_save, sender=User)
def sync_user_profile(sender, instance, created, **kwargs):
    """
    Creates a new user profile or updates the
    existing one for the given user.
    """
    if created:
        Profile.objects.create(user=instance)
    # Otherwise just save for the existing users
    instance.profile.save()
