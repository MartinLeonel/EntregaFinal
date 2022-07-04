from email.policy import default
from django.db import models
from concurrent.futures.process import _MAX_WINDOWS_WORKERS

class Restaurant(models.Model):
    zona = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.FloatField(default=0.0)
    descripcion = models.CharField(max_length=5000)
    carta = {"plato":models.CharField(max_length=100), "precio":models.FloatField(default=0.0), "descripcionplato":models.CharField(max_length=1000)}
    
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"

