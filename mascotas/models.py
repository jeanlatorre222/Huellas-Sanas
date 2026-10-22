from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    nombre_dueno = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    ESTADOS_CHOICES = [
        ("pendiente", "Pendiente"),
        ("atendida", "Atendida"),
        ("cancelada", "Cancelada"),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_CHOICES,
        default="pendiente",
    )

    def __str__(self):
        return f"{self.mascota} - {self.fecha} {self.hora}"