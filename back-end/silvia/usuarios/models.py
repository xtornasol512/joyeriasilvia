from django.db import models
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    asignacion = models.ForeignKey("Rol")
    class Meta:
        verbose_name = "Tipo de Usuario"
        verbose_name_plural = "Tipos de Usuarios"
    def __unicode__(self):
        return "%s -- %s"%(self.usuario, self.asignacion)

class Rol(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    nivel = models.IntegerField(null=True, blank=True)
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
    def __unicode__(self):
        return "%s"%self.descripcion