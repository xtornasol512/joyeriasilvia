from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from proveedores import views

urlpatterns = [
    url(r'^$', views.ProveedorList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProveedorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)