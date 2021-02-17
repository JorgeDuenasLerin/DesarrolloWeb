from django.db import models

# Create your models here.

class Incidencia(models.Model):
    estado = models.CharField(max_length=1,default='a')
    lugar = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.estado + " " + self.lugar
