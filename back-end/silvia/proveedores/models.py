from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length=255)
    direccion = models.TextField(blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    def __unicode__(self):
        return self.nombre

class Telefono(models.Model):
    proveedor = models.ForeignKey("Proveedor")
    descripcion = models.CharField(blank=True, null=True, max_length=255)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    def __unicode__(self):
        return "%s -- %s"%(self.proveedor, self.telefono)
    
    