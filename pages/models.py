from django.db import models

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
        return f'Uploaded {self.title} on {self.updated_at.strftime("%Y-%m-%d %H:%M:%S")}'
