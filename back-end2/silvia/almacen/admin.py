from django.contrib import admin
from almacen.models import Joya, TipoValor, HistorialValor

class JoyaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'proveedor','tipoValor', 'carroCompra', 'regresar' )
    list_filter =('proveedor', 'tipoValor', 'existente')
    search_fields=('id', 'proveedor__clave', 'proveedor__nombre', 'proveedor__correo',
        'proveedor__descripcion', 'fechaCompra')

admin.site.register(Joya, JoyaAdmin)
admin.site.register(TipoValor)
admin.site.register(HistorialValor)

# Register your models here.
