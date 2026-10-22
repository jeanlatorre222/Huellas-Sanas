from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.dateparse import parse_date

from .forms import CitaForm, MascotaForm
from .models import Cita


def index(request):
    return HttpResponse("Clinica Veterinaria")


def listado_citas(request):
    fecha_parametro = request.GET.get("fecha")
    busqueda = request.GET.get("q", "").strip()
    estado_parametro = request.GET.get("estado", "").strip()

    error_fecha = None
    fecha_obj = None

    # Consulta base con relaciones optimizadas
    citas = Cita.objects.select_related("mascota").order_by("fecha", "hora")

    # 1. Filtro por fecha
    if fecha_parametro:
        fecha_obj = parse_date(fecha_parametro)
        if fecha_obj is None:
            error_fecha = "Introduce una fecha válida en formato AAAA-MM-DD."
            citas = Cita.objects.none()
        else:
            citas = citas.filter(fecha=fecha_obj)

    # 2. Filtro por texto (Nombre de mascota o dueño)
    if busqueda:
        citas = citas.filter(
            Q(mascota__nombre__icontains=busqueda)
            | Q(mascota__nombre_dueno__icontains=busqueda)
        )

    # 3. Filtro por estado
    if estado_parametro:
        citas = citas.filter(estado=estado_parametro)

    return render(
        request,
        "mascotas/listado_citas.html",
        {
            "citas": citas,
            "fecha": fecha_obj,
            "fecha_parametro": fecha_parametro,
            "busqueda": busqueda,
            "estado_parametro": estado_parametro,
            "error_fecha": error_fecha,
        },
    )


def registrar_cita_mascota(request):
    if request.method == "POST":
        mascota_form = MascotaForm(request.POST)
        cita_form = CitaForm(request.POST)
        if mascota_form.is_valid() and cita_form.is_valid():
            with transaction.atomic():
                mascota = mascota_form.save()
                cita = cita_form.save(commit=False)
                cita.mascota = mascota
                cita.save()
            return redirect("citas")
    else:
        mascota_form = MascotaForm()
        cita_form = CitaForm()

    return render(
        request,
        "mascotas/registrar.html",
        {"mascota_form": mascota_form, "cita_form": cita_form},
    )