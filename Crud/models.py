from django.db import models

# Create your models here.
class Buses(models.Model):
    modelo = models.CharField(max_length=200, blank=False, null=True)
    marca = models.CharField(max_length=200, blank=False, null=True)
    placa = models.CharField(max_length=200, unique=True, blank=False, null=True)
    año_fabricado = models.DateField(blank=False, null=True)
    motor = models.CharField(max_length=200, unique=True, blank=False, null=True)
    año_modelo = models.DateField(blank=False, null=True)
    chasis = models.CharField(max_length=200, blank=False, null=True)
    kilometraje = models.CharField(max_length=10, blank=False, null=True)
    capacidad_pasajero = models.CharField(max_length=2, blank=False, null=True)
    ruedas = models.CharField(max_length=2, blank=False, null=True)
    ejes = models.CharField(max_length=2, blank=False, null=True)
    Propietario = models.CharField(max_length=100, blank=False, null=True)
    cedula = models.CharField(max_length=10, unique=True ,blank=False, null=True)
    telefono = models.CharField(max_length=10, blank=False, null=True)
    direccion = models.CharField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = "Buses"
        verbose_name_plural = "Buses"
        ordering= ['id']

        def __str__(self):
            return "{}".format(self.modelo)