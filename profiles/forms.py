from django import forms
from .models import Profile

#Order Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Form fields
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Form placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2 (Optional)',
            'default_city': 'City',
            'default_postcode': 'Postal Code',
            'default_county': 'County / Region',
        }


        # Make First name field autofocus
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # Check if the field is required
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *' # Add with star if it's required
                else:
                    placeholder = placeholders[field]

                self.fields[field].widget.attrs['placeholder'] = placeholder # Otherwise placeholder only

                # Remove the default labels from django forms
                self.fields[field].label = False
            else:
                self.fields[field].label = False
