from django import forms
from adverts.models import Advert
#from captcha.fields import CaptchaField

class AdvertCreationForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        fields = ['pet_type', 'start_date',
                  'end_date', 'region', 'price']
        model = Advert
