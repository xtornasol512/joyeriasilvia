from django.contrib import admin
from ventas.models import Venta, ListaJoya, CarroTemporal

class JoyaInLine(admin.TabularInline):
    model = ListaJoya
    extra = 0

class VentaAdmin(admin.ModelAdmin):
    inlines = [JoyaInLine]

admin.site.register(Venta, VentaAdmin)
admin.site.register(CarroTemporal)