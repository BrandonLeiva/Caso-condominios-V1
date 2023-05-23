from django.shortcuts import render
from .models import AreaComun, PagoComun
from .forms import FormAreaComun
# Create your views here.

def inicio(request):
    return render(request, 'myapp/inicio.html')

def ListaResidentes(request):
    return render(request, 'myapp/ListaResidentes.html')

##ÁREAS COMUNES

def AreasAdmin(request):
    data = AreaComun.objects.all()
    return render(request, 'myapp/AreasAdmin.html',{'areas' : data})

def CrearAreas(request):
    data = {
        'form': FormAreaComun()
    }
    if request.method == 'POST':
        form = FormAreaComun(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            data["mensaje"] = "Area común guardada"
        else:
            data["form"] = form
    return render(request, 'myapp/CrearAreas.html', data)

##GASTOS COMUNES

def CrearGastoComun(request):
    data = PagoComun.objects.all()
    return render(request, 'myapp/PagarGastoComun.html',{'Gastos' : data})

def GastoComun(request):
    data = PagoComun.objects.all()
    return render(request, 'myapp/GastoComun.html',{'Gastos' : data})