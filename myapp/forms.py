from django import forms
from .models import AreaComun, PagoComun, Anuncio

class FormAreaComun(forms.ModelForm):
    class Meta:
        model = AreaComun
        fields = ['nombre','descripcion', 'monto','imagen']

        widgets = {
            "fecha": forms.SelectDateWidget()
        }

class FormPagoComun(forms.ModelForm):
    class Meta:
        model = PagoComun
        fields = ['nombre','monto']

class FormAnucio(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo','descripcion']






