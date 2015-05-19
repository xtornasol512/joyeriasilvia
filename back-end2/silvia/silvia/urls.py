from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.auth.models import User

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('home.urls')),
)

if settings.DEBUG:
    urlpatterns+=patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,} ),
    )

    urlpatterns+=patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.STATICFILES_DIRS,} ),
    )