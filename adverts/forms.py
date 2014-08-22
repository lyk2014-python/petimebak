from django import forms
from adverts.models import Advert, AdvertImage

class AdvertCreationForm(forms.ModelForm):

    class Meta:
        fields = ['pet_type', 'start_date',
                  'end_date', 'region', 'price']
        model = Advert


class PhotoCreationForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'image']
        model = AdvertImage
