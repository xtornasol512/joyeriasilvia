from django.db import models
from proveedores.models import Proveedor

from django.db.models.signals import pre_save, post_save
from datetime import date

class Joya(models.Model):
    #calculados en un funcion del guardado anteriormente
    proveedor = models.ForeignKey(Proveedor, blank=True, null=True)
    tipoValor = models.ForeignKey('TipoValor')
    fechaCompra = models.DateField(default=date.today)
    #Rellenado Manual
    peso = models.DecimalField(max_digits=9, decimal_places=3)
    costo = models.DecimalField(max_digits=9, decimal_places=2)
    precioVentaContado = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,
        verbose_name='Precio de venta de Contado')
    precioVentaPagos = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,
        verbose_name='Precio de venta en Pagos')
    #Opcionales no comunes
    foto = models.ImageField(blank=True, null=True, upload_to='asets/items/joyas')

    existente = models.BooleanField(default=True)
    valorGO = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    def __unicode__(self):
        if self.tipoValor.kilataje:
            return "%s %s %s %s %s %s %s"%(self.id, self.proveedor.clave, self.valorGO,
            self.peso, self.tipoValor.kilataje, self.precioVentaContado, self.precioVentaPagos)
        else:
            return "%s %s %s %s %s %s"%(self.id, self.proveedor.clave, self.valorGO,
            self.peso, self.precioVentaContado, self.precioVentaPagos)
    #Metodos de Carro de compra, agregar o eliminar

class TipoValor(models.Model):
    clave = models.CharField(unique=True, max_length=5,
        help_text='Esta clave es la que servira en las etiquetas para identificar al el tipo de Joya')
    kilataje = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2,
        help_text='Valor del gramo Actual, un historial mantiene el valor del gramo el dia que registro las otras joyas')
    nombre = models.CharField(max_length=254, help_text='Nombre o descripcion de la clave')
    def __unicode__(self):
        if self.kilataje:
            return "%s %skts $%s/g %s"%(self.clave, self.kilataje, self.valor, self.nombre)
        else:
            return "%s $%s/g %s"%(self.clave, self.valor, self.nombre)

class HistorialValor(models.Model):
    tipoValor = models.ForeignKey(TipoValor, related_name='tipo_valor')
    fecha = models.DateField(default=date.today)
    valor = models.DecimalField(max_digits=5, decimal_places=2, help_text='Valor del gramo segun el tipo de Joya')
    def __unicode__(self):
        return "%s -- %s $%s"%(self.tipoValor, self.fecha, self.valor)

def update_JoyaValor(sender, instance, **kwargs):
    if not instance.valorGO:
        instance.valorGO=instance.tipoValor.valor

def update_HistorialValor(sender, instance, **kwargs):
    valor=instance.valor
    historial=HistorialValor.objects.filter(tipoValor=instance).order_by("-id")
    if historial:
        ultimo=historial[0]
        if not ultimo.valor == valor:
            his=HistorialValor()
            his.tipoValor=instance
            his.valor=instance.valor
            his.save()
    else:
        his=HistorialValor()
        his.tipoValor=instance
        his.valor=instance.valor
        his.save()

pre_save.connect(update_JoyaValor, sender=Joya, dispatch_uid="update_valor_joya")
post_save.connect(update_HistorialValor, sender=TipoValor, dispatch_uid="update_historial_valores")
