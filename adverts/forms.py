# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from adverts.models import Advert


class AdvertCreationForm(forms.ModelForm):

    class Meta:

        fields = ['pet_type', 'start_date', 'end_date', 'region', 'price']

        model = Advert


    def cleandate(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")

        if end_date < start_date:
            raise ValidationError("Bitiş tarihi başlangıç tarihinden erken olamaz!")