from django.db import models
from clientes.models import Cliente
#from almacen.models import Joya
#from django.contrib.auth.models import User

class CarroTemporal(models.Model):
    #usuario = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente)
