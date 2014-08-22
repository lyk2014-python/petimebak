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
    url(r'^advert/(?P<pk>[\d]+)$', 'adverts.views.detail_advert', name='detail_advert'),
    url(r'^advert/(?P<pk>[\d]+)/photo-add', 'adverts.views.photo_add', name='photo_add'),

    url(r'^advert/(?P<pk>[\d]+)/new-message$', 'messages.views.new_message', name='new_message'),
    url(r'^messages$', 'messages.views.inbox', name='inbox'),
    url(r'^messages/(?P<pk>[\d]+)$', 'messages.views.conversation_detail', name='conversation_detail'),

#    url(r'^captcha/', include('captcha.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
