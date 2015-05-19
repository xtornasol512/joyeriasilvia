from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    notas = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre

class Telefono(models.Model):
    cliente = models.ForeignKey(Cliente)
    telefono = models.CharField(max_length=20)
    tipo = models.ForeignKey("TipoTelefono", blank=True, null=True)

class TipoTelefono(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

class Libreta(models.Model):
    nombre = models.CharField(max_length=254)
    cliente = models.ManyToManyField(Cliente)
    notas = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre
