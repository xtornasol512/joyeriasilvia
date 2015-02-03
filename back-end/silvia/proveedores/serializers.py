from django.forms import widgets
from rest_framework import serializers
from proveedores.models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'nombre', 'direccion', 'correo')

'''class ProveedorSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=False, allow_blank=True, max_length=100)
    direccion = serializers.TextField(style={'type': 'textarea'})
    correo = serializers.EmailField(style={'type': 'email'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Proveedor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.save()
        return instance'''