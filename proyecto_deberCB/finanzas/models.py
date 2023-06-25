from django.db import models

# Create your models here.

class EntidadFinanzas(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    num_sucursales = models.IntegerField()
    ciudad_entidad = models.CharField(max_length=30)
    

    def __str__(self):
        return """Nombre: %s - Siglas: %s \n
                num_sucursales: %d\n
                ciudad_entidad %s""" % (self.nombre,
                self.siglas,
                self.num_sucursales,
                self.ciudad_entidad)
