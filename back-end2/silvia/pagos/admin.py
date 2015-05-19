from django.contrib import admin
from pagos.models import Deuda, ListaVenta, HistorialPago
class VentaInLine(admin.TabularInline):
    model = ListaVenta
    extra = 1

class PagoInLine(admin.TabularInline):
    model = HistorialPago
    extra = 1

class DeudasAdmin(admin.ModelAdmin):
    inlines = [VentaInLine, PagoInLine]

admin.site.register(Deuda, DeudasAdmin)