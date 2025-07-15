from django import forms
from .models import Product, Category
from django.utils.safestring import mark_safe



# Size choices
SIZE_CHOICES = [(str(i), str(i)) for i in range(38, 47)]


# Form for product management
class ProductForm(forms.ModelForm):
    size = forms.ChoiceField(
        choices=[('', 'Select a size')]+ SIZE_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Product
        exclude = ('image_url',)

    def clean(self):
        cleaned_data = super().clean()
        free_size = cleaned_data.get('free_size')
        sizes = cleaned_data.get('size')
        category = cleaned_data.get('category')

        if category is None:
            raise forms.ValidationError("Please select a category.")

        # Prevent both size and free size being set
        if free_size and sizes:
            raise forms.ValidationError(
                "Select either Free Size or specific sizes, not both."
            )
        # Prevent neither being set
        if not free_size and (not sizes or len(sizes) == 0):
            raise forms.ValidationError(
                "Please select at least one size or check Free Size."
            )
        # Ensure 'size' is always stored as a list.
        if sizes and isinstance(sizes, str):
            cleaned_data['size'] = [sizes]
        else:
            cleaned_data['size'] = sizes or []

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Order the queryset explicitly
        self.fields['category'].queryset = Category.objects.order_by(
            'friendly_name'
        )

        # Override the category to display the category firendly name
        self.fields['category'].label_from_instance =lambda obj: obj.friendly_name or obj.name
        self.fields['category'].empty_label = 'Select Category'

        # Customise description textarea
        self.fields['description'].widget.attrs.update(
            {
                'rows': 4,
                'class': 'form-control',
            }
        )

        # Customize the label for the 'free_size' checkbox by adding
        # left padding using a <span>.
        self.fields['free_size'].label = mark_safe('<span style="padding-left: 10px;">Free Size</span>')

        # Give the name field autofocus style
        self.fields['name'].widget.attrs['autofocus'] = True