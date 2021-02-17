from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    hora = models.IntegerField()
    creditos = models.IntegerField()
    estado = models.BooleanField()


class Carrera(models.Model):
    nombre = models.CharField(max_length=20)
    nombrecorto = models.CharField(max_length=30)
    image = models.ImageField(default = 'null')
    estado = models.BooleanField()
    
