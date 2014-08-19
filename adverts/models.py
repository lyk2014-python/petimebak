# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode


class PetType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        verbose_name = "Pet Tipi"
        verbose_name_plural = "Pet Tipleri"

class Advert(models.Model):
    region = models.CharField(max_length=255)
    pet_type = models.ForeignKey("PetType")
    user = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return smart_unicode("%s -> %s " %(self.user.username, self.pet_type.name))

    class Meta:
        verbose_name = "İlan"
        verbose_name_plural = "İlanlar"