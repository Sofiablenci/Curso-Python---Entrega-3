from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)

    def __str__(self):
        return f'Libro ({self.id}): {self.titulo} - {self.genero}'