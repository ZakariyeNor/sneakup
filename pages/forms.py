from django import forms
from .models import ContactMessage

# Create contact form
class ContactMessageForm(forms.ModelForm):
    """
    Form for users to submit contact messages to customer support.
    """

    class Meta:
        model = ContactMessage
        fields = (
            'full_name', 'email', 'order_number',
            'message', 'send_info', 'created_at',
        )
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Type your message here...',
                'rows': 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Customize field placeholders and remove labels for a cleaner UI.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': "Email Address",
            'order_number': 'Order Number (optional)',
        }

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]

            # Optional: remove labels and use placeholders only
            self.fields[field].label = ''
