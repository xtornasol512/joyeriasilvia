from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    def __unicode__(self):
        return self.nombre

class HistorialPago(models.Model):
    cliente = models.ForeignKey("Cliente")
    fecha = models.DateField(auto_now=True)
    abono = models.DecimalField(max_digits=8, decimal_places=2)
    def __unicode__(self):
        return "%s %s $%s, restan:%s"%(self.cliente, self.fecha, self.abono, "Resta")
    
class Deuda(models.Model):
    cliente = models.ForeignKey(Cliente)
    deuda = models.DecimalField(max_digits=9, decimal_places=2)
    def __unicode__(self):
        return "%s, Deuda: $%s"%(self.cliente, self.deuda)
    
