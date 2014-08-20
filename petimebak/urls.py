from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'adverts.views.home', name='home'),
    url(r'^login$', 'profiles.views.login', name='login'),
    url(r'^logout', 'profiles.views.logout', name='logout'),
    url(r'^register', 'profiles.views.register', name='register'),

    url(r'^new', 'adverts.views.new_advert', name='new_advert'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
