from django import forms
from .models import Product, Category

# Form for product management
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Order the queryset explicitly
        self.fields['category'].queryset = Category.objects.order_by(
            'friendly_name'
            )

        # Override the category to display the category firendly name
        self.fields['category'].label_from_instance =lambda obj: obj.friendly_name or obj.name
