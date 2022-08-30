from distutils.command.upload import upload
from django.db import models


class juego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="juegoteca/imagenes/")
    url = models.URLField(blank=True)
