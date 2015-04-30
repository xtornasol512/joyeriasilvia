from django.db import models

class Proveedor(models.Model):
    clave = models.CharField(unique=True, max_length=4,
        help_text='Esta clave es la que servira en las etiquetas para identificar al proveedor')
    nombre = models.CharField(blank=True, null=True, max_length=255)
    descripcion = models.TextField(blank=True, null=True,
        help_text='Puede escribir Direcciones o anotaciones personales sobre este proveedor')
    correo = models.EmailField(blank=True, null=True)
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    def __unicode__(self):
        return self.nombre

class Telefono(models.Model):
    proveedor = models.ForeignKey("Proveedor")
    telefono = models.CharField(blank=True, null=True, max_length=20)
    descripcion = models.CharField(blank=True, null=True, max_length=255)
    def __unicode__(self):
        return "%s -- %s"%(self.proveedor, self.telefono)
    
    