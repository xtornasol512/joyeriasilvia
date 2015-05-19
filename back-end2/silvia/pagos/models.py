from django.db import models
from ventas.models import Venta

class Deuda(models.Model):
    nombre = models.CharField(max_length=255)
    def __unicode__(self):
        return self.nombre

class ListaVenta(models.Model):
    deuda = models.ForeignKey(Deuda)
    venta = models.ForeignKey(Venta)

class HistorialPago(models.Model):
    deuda = models.ForeignKey(Deuda)
    abono = models.DecimalField(max_digits=9, decimal_places=2)
    fecha = models.DateField(auto_now=True)
    notas = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s $%s -- %s"%(self.deuda, self.abono, self.fecha)