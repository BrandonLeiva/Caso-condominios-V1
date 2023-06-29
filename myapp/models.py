from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    imagen = models.ImageField(upload_to="FotoPerfil", default='ImagenUsuario.webp', null=True)
    direccion = models.CharField(max_length=50)
    num_telefono = models.CharField(max_length=50)
    fecha_naci = models.DateField(null=True)
    gastos_comunes = models.ManyToManyField('PagoComun', related_name='residentes', blank=True)

    def __str__(self):
        return self.username 


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
    descripcion = models.TextField()
    monto = models.IntegerField()
    fecha = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to="areas", null=True)
    def __str__(self):
        return self.nombre 
    
    
class Anuncio(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField(default=date.today)
    def __str__(self):
        return self.titulo 
    
class Multa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Motivo = models.TextField()
    monto = models.IntegerField()
    fecha = models.DateField(default=date.today)
    ESTADO_PAGO = (
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        # Agrega más opciones de estado de pago si es necesario
    )
    estado = models.CharField(max_length=20, choices=ESTADO_PAGO, default='Pendiente')