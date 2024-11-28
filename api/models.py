from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Cliente(models.Model):
    # Tipos de Genero
    GENERO_CHOICES = [
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    ]
    # Niveles de satisfaccion 1-5
    NIVEL_DE_SATISFACCION = [
        (1,'Muy insatisfecho'),
        (2,'Insatisfecho'),
        (3,'Neutro'),
        (4,'Satisfecho'),
        (5,'Muy satisfecho'),
    ]
    # Cliente ID se auto incrementa cada vez que se agrega uno nuevo
    cliente_id = models.AutoField(primary_key=True)
    edad = models.PositiveSmallIntegerField()
    genero = models.CharField(max_length=9 ,choices= GENERO_CHOICES)
    saldo = models.FloatField(validators=[MinValueValidator(0)])
    active = models.BooleanField()
    nivel_de_satisfaccion = models.FloatField(choices= NIVEL_DE_SATISFACCION)

    def __str__ (self):
        return f"Cliente ID: {self.cliente_id}"