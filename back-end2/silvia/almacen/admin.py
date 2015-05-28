from django.contrib import admin
from almacen.models import Joya, TipoValor, HistorialValor

class JoyaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )

admin.site.register(Joya, JoyaAdmin)
admin.site.register(TipoValor)
admin.site.register(HistorialValor)

# Register your models here.
