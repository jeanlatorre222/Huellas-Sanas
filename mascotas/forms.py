from django import forms

from .models import Cita, Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ("nombre", "especie", "raza", "nombre_dueno")
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "especie": forms.TextInput(attrs={"class": "form-control"}),
            "raza": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_dueno": forms.TextInput(attrs={"class": "form-control"}),
        }


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ("fecha", "hora", "motivo", "estado")
        widgets = {
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "hora": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "motivo": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }
