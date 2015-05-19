from django.db import models
from clientes.models import Cliente
from almacen.models import Joya
from django.contrib.auth.models import User

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    contado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)
    notas = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s %s"%(self.cliente, self.fecha)

class ListaJoya(models.Model):
    venta = models.ForeignKey(Venta)
    joya = models.ForeignKey(Joya)

class CarroTemporal(models.Model):
    usuario = models.ForeignKey(User)
    joya = models.ForeignKey(Joya)
    venta = models.ForeignKey(Venta)
