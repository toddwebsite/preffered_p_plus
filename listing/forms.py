from django import forms

from .models import Listing


class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('image', 'price', 'bedrooms', 'bathrooms', 'square_feet', 'acres',
        'mls_number', 'built_in', 'agent', 'name', 'street', 'city', 'state', 'zipcode', 'county',
        'desription', 'school_district', 'elementary_sch', 'middle_sch',
        'high_sch', 'available', 'sold', 'price_reduced', 'motivated',)

        widgets = {'agent': forms.HiddenInput(), }
        