from django import forms
from .models import AreaComun, PagoComun, Anuncio, Multa, User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ('username', 'first_name', 'last_name', 'email','imagen','direccion','num_telefono','fecha_naci', 'password1', 'password2')

        widgets = {
            "fecha_naci": forms.SelectDateWidget()
        }


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

class FormMulta(forms.ModelForm):
    class Meta:
        model = Multa
        fields = ['usuario','Motivo','monto']








