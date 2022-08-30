import datetime
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descipcion = models.TextField()
    imange = models.ImageField(upload_to="blog/imagenes")
    fecha = models.DateField(datetime.date.today)
