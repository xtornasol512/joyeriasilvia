from django.db import models
from proveedores.models import Proveedor

from django.db.models.signals import pre_save, post_save
from datetime import date

class Temporal(models.Model):
    idProv = models.IntegerField(blank=True, null=True)
    idTipo = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(default=date.today)

def ultProv():
    temporal =Temporal.objects.all()
    #temporal=False
    if temporal:
        tem = temporal [0]
        return tem.idProv
    else:
        return None

def ultTipo():
    temporal =Temporal.objects.all()
    #temporal=False
    if temporal:
        tem = temporal [0]
        return tem.idTipo
    else:
        return None

def ultFecha():
    temporal =Temporal.objects.all()
    #temporal=False
    if temporal:
        tem = temporal [0]
        return tem.fecha
    else:
        return date.today

class Joya(models.Model):
    clave = models.CharField(blank=True, null=True, max_length=15,
        help_text='Este campo se Genera automaticamente despues de guardarse los datos')
    #calculados en un funcion del guardado anteriormente
    proveedor = models.ForeignKey(Proveedor, blank=True, null=True, default=ultProv())
    tipoJoya = models.ForeignKey('TipoJoya', default=ultTipo())
    fechaCompra = models.DateField(default=ultFecha())

    #Rellenado Manual
    peso = models.DecimalField(max_digits=9, decimal_places=3)
    costo = models.DecimalField(max_digits=9, decimal_places=2)
    precioVentaContado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
        verbose_name='Precio de venta de Contado')
    precioVentaPagos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
        verbose_name='Precio de venta en Pagos')
    #Opcionales no comunes    
    nombre = models.CharField(blank=True, null=True, max_length=150)
    foto = models.ImageField(blank=True, null=True, upload_to='asets/items/joyas')
    existente = models.BooleanField(default=True)
    def __unicode__(self):
        return self.clave

class TipoJoya(models.Model):
    clave = models.CharField(unique=True, max_length=5,
        help_text='Esta clave es la que servira en las etiquetas para identificar al el tipo de Joya')
    nombre = models.CharField(max_length=100, help_text='Puede ser el tipo de oro y su kilatage')
    descripcion = models.TextField(blank=True, null=True,
        help_text='Si el nombre no es suficiente, aqui puede escribir la descripcion detallada')
    valor = models.DecimalField(max_digits=5, decimal_places=2,
        help_text='Valor del gramo Actual, un historial mantiene el valor del gramo el dia que registro las otras joyas')
    class Meta:
        verbose_name = "Tipo de Joya"
        verbose_name_plural = "Tipos de Joyas"
    def __unicode__(self):
        return "%s - %s"%(self.clave, self.nombre)

class Valor(models.Model):
    tipoJoya = models.ForeignKey(TipoJoya, related_name='tipo_joya')
    fecha = models.DateField(default=date.today)
    valor = models.DecimalField(max_digits=5, decimal_places=2, help_text='Valor del gramo segun el tipo de Joya')
    notas = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Valor"
        verbose_name_plural = "Valores"

    def __str__(self):
        pass
    

def update_Joya_pre(sender, instance, **kwargs):
    #clave, datos temporales del ultimo registro, asignacion del control de valor
   
    #datos temporales
    temporal =Temporal.objects.all()
    #temporal=False
    if temporal:
        tem = temporal [0]
    else:
        tem=Temporal()
    tem.idProv=instance.proveedor.id
    tem.idTipo=instance.tipoJoya.id
    tem.fecha=instance.fechaCompra
    tem.save()

    #Clave
    #ultimo id+1
    instance.clave="id %s %s %s %s %s"%(instance.proveedor.clave, instance.tipoJoya.clave, instance.peso,
        instance.precioVentaContado, instance.precioVentaPagos)

def update_Joya_post():
    #funsion no programada aun
    pass

pre_save.connect(update_Joya_pre, sender=Joya, dispatch_uid="pre_update_datos_Joya")
#post_save.connect(update_Joya_post, sender=Joya, dispatch_uid="post_update_datos_Joya")