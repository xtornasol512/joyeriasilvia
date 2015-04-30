from django.contrib import admin
from proveedores.models import Proveedor, Telefono

class TelefonoInLine(admin.TabularInline):
    model = Telefono
    extra = 2

class ProveedorAdmin(admin.ModelAdmin):
    inlines = [TelefonoInLine]

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Telefono)

# Register your models here.
