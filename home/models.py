from django.db import models

# Email subscription model
class NewsletterSubscriber(models.Model):
    """
    Stores email addresses of users who subscribed to the newsletter,
    so we can send them marketing emails later.
    """
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} | subscribed on {self.created_at.strftime("%Y-%m-%d")}'
