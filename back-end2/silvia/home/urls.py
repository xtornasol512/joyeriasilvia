from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('home.views',
    url(r'^$','index'),
    url(r'^home/$','home_v'),
    url(r'^venta/$','venta'),
    url(r'^logout/$','log_out'),
    url(r'^venta/addCarro$','ventaAdd'),
    #url(r'^tag/(?P<tag>[\w\-]+)/$','tag_aviso'),
    #url(r'^(?P<perfil>[\w\-]+)/$','perfil_view'),
)