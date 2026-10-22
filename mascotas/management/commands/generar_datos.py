import random
from datetime import time, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from mascotas.models import Cita, Mascota


class Command(BaseCommand):
    help = "Genera datos ficticios de mascotas y citas."

    def handle(self, *args, **options):
        nombres_mascotas = [
            "Luna", "Max", "Nala", "Rocky", "Milo",
            "Coco", "Bella", "Toby", "Simba", "Lola",
            "Bruno", "Mia", "Duke", "Kira", "Oliver",
            "Daisy", "Leo", "Canela", "Tina", "Thor",
        ]
        nombres_duenos = [
            "Ana García", "Luis Pérez", "María López", "Carlos Ruiz",
            "Sofía Torres", "Diego Flores", "Valentina Díaz",
            "Javier Romero", "Camila Herrera", "Mateo Castro",
        ]
        razas_por_especie = {
            "perro": ["Labrador", "Caniche", "Beagle", "Mestizo", "Pastor alemán"],
            "gato": ["Siamés", "Persa", "Maine Coon", "Angora", "Doméstico"],
        }
        motivos = [
            "Control general", "Vacunación", "Revisión dental",
            "Consulta de rutina", "Revisión de piel",
        ]
        estados = ["pendiente", "atendida", "cancelada"]
        fecha_actual = timezone.localdate()

        with transaction.atomic():
            mascotas = []
            for nombre in nombres_mascotas:
                especie = random.choice(["perro", "gato"])
                mascotas.append(
                    Mascota.objects.create(
                        nombre=nombre,
                        especie=especie,
                        raza=random.choice(razas_por_especie[especie]),
                        nombre_dueno=random.choice(nombres_duenos),
                    )
                )

            for indice in range(20):
                fecha = (
                    fecha_actual
                    if indice == 0
                    else fecha_actual + timedelta(days=random.randint(-15, 15))
                )
                Cita.objects.create(
                    mascota=random.choice(mascotas),
                    fecha=fecha,
                    hora=time(hour=9 + (indice % 8), minute=random.choice([0, 30])),
                    motivo=random.choice(motivos),
                    estado=estados[indice % len(estados)],
                )

        self.stdout.write(
            self.style.SUCCESS("Se generaron 20 mascotas y 20 citas correctamente.")
        )
