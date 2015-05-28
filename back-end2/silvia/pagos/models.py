from django.db import models
from ventas.models import Venta

class Cuenta(models.Model):
    nombre = models.CharField(max_length=255)
    def __unicode__(self):
        return self.nombre

class ListaVenta(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    venta = models.ForeignKey(Venta)

class HistorialPago(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    abono = models.DecimalField(max_digits=9, decimal_places=2)
    fecha = models.DateField(auto_now=True)
    notas = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s $%s -- %s"%(self.cuenta, self.abono, self.fecha)