from django import forms
from .models import AreaComun

class FormAreaComun(forms.ModelForm):
    class Meta:
        model = AreaComun
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget()
        }