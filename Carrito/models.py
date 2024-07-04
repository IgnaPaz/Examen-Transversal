from django.db import models

class Catalogo(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='Catalogos/', null= True)

    def __str__(self):
        return self.nombre

