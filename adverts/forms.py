from django import forms
from adverts.models import Advert


class AdvertCreationForm(forms.ModelForm):
    class Meta:
        fields = ['pet_type', 'start_date',
                  'end_date', 'region', 'price']
        model = Advert