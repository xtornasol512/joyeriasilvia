from proveedores.models import Proveedor
from proveedores.serializers import ProveedorSerializer
from rest_framework import generics
from rest_framework import permissions

# Vistas en forma de Clases Genericas
class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


#recordar que las vistas pueden ser echas en forma clasica, con decoradores, en forma de clase y clases Genericas
#segun las nesecidades requeridas.