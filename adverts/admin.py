from django.contrib import admin

from adverts.models import Advert, PetType, AdvertImage


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('user', 'region',
                    'pet_type', 'date_created',
                    'is_published')
    list_filter = ('price', 'user')
    search_fields = ('user__username', 'region', 'pet_type__name')
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        queryset.update(is_published=True)

    mark_as_published.short_description = "Secili ilanlari yayinla"

class PetTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advert, AdvertAdmin)
admin.site.register(AdvertImage)
admin.site.register(PetType, PetTypeAdmin)
