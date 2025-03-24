from django.db import models

class Reservas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 255)
    cantidad_invitados = models.IntegerField()
    fecha_reserva = models.DateTimeField()


class Menus(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    inventario = models.IntegerField()
