from django.conf.urls import url
from proveedores import views

urlpatterns = [
    url(r'^$', views.proveedores_lista),
    url(r'^(?P<pk>[0-9]+)/$', views.proveedor_detalle),
]