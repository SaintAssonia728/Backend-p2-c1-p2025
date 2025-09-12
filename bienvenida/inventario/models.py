from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    precio = models.DecimalField(decimal_places=2, max_digits=9999)
    stock = models.IntegerField(default=0)
