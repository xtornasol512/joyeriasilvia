from django.contrib import admin
from clientes.models import Cliente, Telefono, Libreta
class TelefonoInLine(admin.TabularInline):
    model = Telefono
    extra = 2

class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoInLine]
    list_display = ('__unicode__','notas', 'seleccionar' )


class LibretasAdmin(admin.ModelAdmin):
    filter_horizontal =('cliente',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefono)
admin.site.register(Libreta, LibretasAdmin)