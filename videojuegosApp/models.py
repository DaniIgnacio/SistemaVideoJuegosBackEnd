from django.db import models

# Create your models here.
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fehca_fundacion = models.DateField()

    def __str__(self):
        fila = self.nombre
        return fila

    

class Juego(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='static/img/')
    genero = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)