from django import forms
from .models import AreaComun, PagoComun, Anuncio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

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








