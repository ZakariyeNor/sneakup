from django import forms
from .models import Product, Category
from django.utils.safestring import mark_safe



# Size choices
SIZE_CHOICES = [(str(i), str(i)) for i in range(38, 47, 1)]


# Form for product management
class ProductForm(forms.ModelForm):
    size = forms.MultipleChoiceField(
        choices=SIZE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Available Sizes (38-46, step 2)"
    )
    free_size = forms.BooleanField(
        required=False,
        label="Free Size (one-size-fits-all)"
    )

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        free_size = cleaned_data.get('free_size')
        sizes = cleaned_data.get('size')
        category = cleaned_data.get('category')

        if category is None:
            raise forms.ValidationError("Please select a category.")

        # Validation logic
        if free_size and sizes:
            raise forms.ValidationError("Choose either specific sizes or Free Size — not both.")
        if not free_size and not sizes:
            raise forms.ValidationError("You must either select at least one size or check Free Size.")

        
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

        