from django.shortcuts import render, redirect, get_object_or_404
from .models import AreaComun, PagoComun, Anuncio
from .forms import FormAreaComun, FormPagoComun, FormAnucio
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.

def inicio(request):
    return render(request, 'myapp/inicio.html')

def ListaResidentes(request):
    users = User.objects.exclude(is_superuser=True)
    return render(request, 'myapp/ListaResidentes.html',{'users' : users})

##ÁREAS COMUNES

def AreasAdmin(request):
    data = AreaComun.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(data, 8)
        data = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'myapp/Areas/AreasAdmin.html',{'entity' : data, 'paginator':paginator})



def CrearAreas(request):
    data = {
        'form': FormAreaComun()
    }
    if request.method == 'POST':
        form = FormAreaComun(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to=AreasAdmin)
        else:
            data["form"] = form
    return render(request, 'myapp/Areas/CrearAreas.html', data)

##GASTOS COMUNES


def GastoComun(request):
    data = PagoComun.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(data, 10)
        data = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'myapp/GastosComunes/GastoComun.html',{'entity' : data, 'paginator':paginator})


def CrearGastoComun(request):
    data = {
        'form': FormPagoComun()
    }
    if request.method == 'POST':
        form = FormPagoComun(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to=GastoComun)
        else:
            data["form"] = form
    return render(request, 'myapp/GastosComunes/CrearGastoComun.html', data)


##FOROS

def Foro(request):
    data = Anuncio.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(data, 2)
        data = paginator.page(page)
    except:
        raise Http404
    return render(request, 'myapp/Anuncios/Foro.html',{'entity' : data,  'paginator':paginator})

def CrearAnuncio(request):
    data = {
        'form': FormAnucio()
    }
    if request.method == 'POST':
        form = FormAnucio(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to=Foro)
        else:
            data["form"] = form
    return render(request, 'myapp/Anuncios/CrearAnuncio.html', data)

def ModificarAnucio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)

    data = {
        'form': FormAnucio(instance=anuncio)
    }

    if request.method == 'POST':
        form = FormAnucio(data=request.POST, files=request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to=Foro)
        else:
            data["form"] = form

    return render(request, 'myapp/Anuncios/ModificarAnuncio.html', data)