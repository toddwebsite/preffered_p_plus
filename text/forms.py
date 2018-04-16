from django import forms
# import string


# from hourly.models import Hourly
from .models import Details
# from source_utils.form_mixins import check_name


class SiteDataForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('caption', 'bio', 'image', 'phone_number',
        'email', 'alt_phone_number', 'text_color',)

        # widgets = {'image': forms.Select(attrs={'rows':2,}), }
        
    def clean(self):
        """
        Handles validation.
        """
        # print(self)
        pass
        # return string.capwords(check_name(self.cleaned_data["pricing"]))