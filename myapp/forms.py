from django import forms
from .models import AreaComun

class FormAreaComun(forms.ModelForm):
    class Meta:
        model = AreaComun
        fields = ['nombre', 'estado_reserva', 'descripcion', 'monto', 'fecha','imagen']

        widgets = {
            "fecha": forms.SelectDateWidget()
        }

