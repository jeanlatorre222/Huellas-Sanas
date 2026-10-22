from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_citas, name='citas'),
    path('registrar/', views.registrar_cita_mascota, name='registrar'),
]