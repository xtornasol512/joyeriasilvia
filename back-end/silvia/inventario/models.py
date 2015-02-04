from django.db import models
from proveedores.models import Proveedor

class Joya(models.Model):
    clave = models.CharField(max_length=15)
    nombre = models.CharField(blank=True, null=True, max_length=150)
    foto = models.ImageField(blank=True, null=True, upload_to='asets/items/joyas')
    peso = models.DecimalField(max_digits=9, decimal_places=3)
    kilataje = models.ForeignKey("Kilataje", blank=True, null=True)
    tipoOro = models.ForeignKey("TipoOro", blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor)
    costo = models.DecimalField(max_digits=9, decimal_places=2)
    precioOroCompra = models.DecimalField(max_digits=5, decimal_places=2)
    fechaCompra = models.DateField()
    def __unicode__(self):
        return self.clave

class Kilataje(models.Model):
    kilataje = models.CharField(max_length=50)
    def __unicode__(self):
        return self.kilataje

class TipoOro(models.Model):
    descripcion = models.CharField(max_length=255)
    precioActual = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        verbose_name = "Tipo deOro"
        verbose_name_plural = "Tipos de Oro"
    def __unicode__(self):
        return "%s $%s"%(self.descripcion, self.precioActual)
