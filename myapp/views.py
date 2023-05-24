from django.shortcuts import render
from .models import AreaComun, PagoComun, Anuncio
from .forms import FormAreaComun
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def inicio(request):
    return render(request, 'myapp/inicio.html')

def ListaResidentes(request):
    return render(request, 'myapp/ListaResidentes.html')

def Foro(request):
    data = Anuncio.objects.all()
    return render(request, 'myapp/Foro.html',{'anuncios' : data})

##ÁREAS COMUNES

def AreasAdmin(request):
    data = AreaComun.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(data, 6)
        data = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'myapp/AreasAdmin.html',{'entity' : data, 'paginator':paginator})



def CrearAreas(request):
    data = {
        'form': FormAreaComun()
    }
    if request.method == 'POST':
        form = FormAreaComun(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado correctamente")
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