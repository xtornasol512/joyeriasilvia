from django.contrib import admin
from clientes.models import Cliente, HistorialPago, Deuda
admin.site.register(Cliente)
admin.site.register(HistorialPago)
admin.site.register(Deuda)