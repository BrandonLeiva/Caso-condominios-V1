from django.shortcuts import render, redirect, get_object_or_404
from .models import AreaComun, PagoComun, Anuncio, Multa, User
from .forms import FormAreaComun, FormPagoComun, FormAnucio, FormMulta, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def inicio(request):
    return render(request, 'myapp/inicio.html')

# VISTAS DE USUARIOS

def UsuariosGastosComunes(request):
    return render(request, 'myapp/GastosComunes/UsuarioConGasto.html')

@login_required
def Perfil(request):
    usuario = request.user
    data = Multa.objects.filter(usuario=request.user)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(data, 3)
        data = paginator.page(page)
    except:
        raise Http404
    return render(request, 'myapp/PerfilUsuario/PerfilUsuario.html', {'users' : usuario, 'entity' : data, 'paginator':paginator})

def ModificarPerfil(request, id):
    anuncio = get_object_or_404(User, id=id)

    data = {
        'form': CustomUserCreationForm(instance=anuncio)
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST, files=request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to=Foro)
        else:
            data["form"] = form

    return render(request, 'myapp/Anuncios/ModificarAnuncio.html', data)

@permission_required('myapp.view_User')
def VerPerfil(request, usuario_id):
    users = get_object_or_404(User, id=usuario_id)
    multas = Multa.objects.filter(usuario=users)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(multas, 3)
        multas = paginator.page(page)
    except:
        raise Http404
    return render(request, 'myapp/PerfilUsuario/PerfilUsuario.html', {'users': users, 'entity': multas, 'paginator':paginator})

@permission_required('myapp.view_User')
def ListaResidentes(request):
    users = User.objects.exclude(is_superuser=True)
    return render(request, 'myapp/ListaResidentes.html', {'users' : users})

def Registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to=inicio)
        else:
            data["form"] = form

    return render(request, 'Registration/registro.html', data)

##ÁREAS COMUNES
@login_required
def AreasAdmin(request):
    data = AreaComun.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(data, 8)
        data = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'myapp/Areas/AreasAdmin.html',{'entity' : data, 'paginator':paginator})


@permission_required('myapp.add_AreaComun')
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

def ReservarArea(request, area_id):
    area = AreaComun.objects.get(pk=area_id)

    if request.method == 'POST':
        area.estado_reserva = 'Reservado'
        area.save()
        return redirect('detalle_area', area_id=area.id)

    context = {
        'areas': area
    }
    return render(request, 'myapp/Areas/ReservarArea.html', context)



##GASTOS COMUNES

@login_required
def GastoComun(request):
    data = PagoComun.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(data, 10)
        data = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'myapp/GastosComunes/GastoComun.html',{'entity' : data, 'paginator':paginator})

def MiGastoComun(request):
    user = request.user
    gastos_comunes = PagoComun.objects.filter(residentes=user)
    return render(request, 'myapp/GastosComunes/MisGastosComunes.html', {'entity': gastos_comunes})

@permission_required('myapp.add_GastoComun')
def CrearGastoComun(request):
    if request.method == 'POST':
        form = FormPagoComun(request.POST)
        if form.is_valid():
            gasto = form.save()
            messages.success(request, "Agregado correctamente")
            # Agregar el gasto común a todos los residentes
            residents = User.objects.filter(is_superuser=False)
            for resident in residents:
                resident.gastos_comunes.add(gasto)
            return redirect('GastoComun')
    else:
        form = FormPagoComun()
    return render(request, 'myapp/GastosComunes/CrearGastoComun.html', {'form': form})

def UsuariosGastosComunes(request, gasto_id):
    gasto = get_object_or_404(PagoComun, pk=gasto_id)
    residentes = gasto.residentes.all()
    return render(request, 'myapp/GastosComunes/UsuarioConGasto.html', {'gasto': gasto, 'residentes': residentes})

def PagarGasto(request, pago_id):
    pagoComun = PagoComun.objects.get(pk=pago_id)

    if request.method == 'POST':
        pagoComun.estado_reserva = 'Pagado'
        pagoComun.save()
        return redirect('detalle_area', pago_id=pago_id)

    context = {
        'entity': pagoComun
    }
    return render(request, 'myapp/GastosComunes/PagarGasto.html', context)


##FOROS
@login_required
def Foro(request):
    data = Anuncio.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(data, 3)
        data = paginator.page(page)
    except:
        raise Http404
    return render(request, 'myapp/Anuncios/Foro.html',{'entity' : data,  'paginator':paginator})

@permission_required('myapp.add_Anuncio')
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

@permission_required('myapp.change_Anuncio')
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

@permission_required('myapp.delete_Anuncio')
def EliminarAnuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    anuncio.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to=Foro)


##MULTAS
@permission_required('myapp.add_Multa')
def CrearMulta(request):
    data = {
        'form': FormMulta()
    }
    if request.method == 'POST':
        form = FormMulta(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to=ListaResidentes)
        else:
            data["form"] = form
    return render(request, 'myapp/Multas/CrearMulta.html', data)

def PagarMulta(request, multa_id):
    multa = Multa.objects.get(pk=multa_id)
    
    if request.method == 'POST':
        # Procesar el pago y actualizar el estado de pago de la multa
        multa.estado_pago = 'Pagado'
        multa.save()
        return redirect(to=Perfil)

    context = {
        'entity': multa
    }
    return render(request, 'myapp/Multas/PagarMulta.html', context)

