from django.contrib import admin
from almacen.models import Joya, TipoJoya

class JoyaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )

admin.site.register(Joya, JoyaAdmin)
admin.site.register(TipoJoya)

# Register your models here.
