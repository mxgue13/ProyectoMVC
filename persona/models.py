from django.db import models
from django.db.models.fields import CharField

# Create your models here.

#entidad tipoDocumento
class Tdocumento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=40)

#entidad ciudad
class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=30)

#entidad persona
class Persona(models.Model):
    idtipoDocumento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    documento = models.CharField(max_length=30)
    fechanacimiento = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)