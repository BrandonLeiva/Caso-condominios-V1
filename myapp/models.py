from django.db import models
from datetime import date

# Create your models here.

class status(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class PagoComun(models.Model):
    ESTADO_PAGO = (
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        # Agrega más opciones de estado de pago si es necesario
    )
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO, default='Pendiente')
    nombre = models.CharField(max_length=50)
    monto = models.IntegerField()
    fecha = models.DateField(default=date.today)
    def __str__(self):
        return self.nombre 
    

class AreaComun(models.Model):
    ESTADO_RESERVA = (
        ('Disponible', 'Disponible'),
        ('Reservado', 'Reservado'),
        # Agrega más opciones de estado de pago si es necesario
    )
    estado_reserva = models.CharField(max_length=20, choices=ESTADO_RESERVA, default='Disponible')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    monto = models.IntegerField()
    fecha = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to="areas", null=True)
    def __str__(self):
        return self.nombre 
    
class Anuncio(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=date.today)
    def __str__(self):
        return self.titulo 