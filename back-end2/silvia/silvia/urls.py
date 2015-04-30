from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.models import User

admin.autodiscover()



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
