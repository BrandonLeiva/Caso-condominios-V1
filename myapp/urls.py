from django.urls import path
from .views import inicio, AreasAdmin, CrearAreas, GastoComun, CrearGastoComun, ListaResidentes, Foro, CrearAnuncio, ModificarAnucio, EliminarAnuncio, Registro, CrearMulta, Perfil, VerPerfil, UsuariosGastosComunes, MiGastoComun, ModificarPerfil, OrdenPagoComun, CapturarPagoComun

urlpatterns = [
    path('',inicio,name="inicio"),
    path('Registro/',Registro,name="Registro"),
    path('AreasAdmin/',AreasAdmin,name="AreasAdmin"),
    path('CrearAreas/',CrearAreas,name="CrearAreas"),
    path('GastoComun/',GastoComun,name="GastoComun"),
    path('CrearGastoComun/',CrearGastoComun,name="CrearGastoComun"),
    path('MiGastoComun/',MiGastoComun,name="MiGastoComun"),
    path('ListaResidentes/',ListaResidentes,name="ListaResidentes"),
    path('Foro/',Foro,name="Foro"),
    path('CrearAnuncio/',CrearAnuncio,name="CrearAnuncio"),
    path('Modificar-Anuncio/<id>/',ModificarAnucio,name="ModificarAnucio"),
    path('Eliminar-Anuncio/<id>/',EliminarAnuncio,name="EliminarAnuncio"),
    path('CrearMulta/',CrearMulta,name="CrearMulta"),
    path('Perfil/',Perfil,name="Perfil"),
    path('Modificar-Perfil/<id>/',ModificarPerfil,name="ModificarPerfil"),
    path('VerPerfil/<int:usuario_id>/',VerPerfil,name="VerPerfil"),
    path('UsuariosGastosComunes/<int:gasto_id>/',UsuariosGastosComunes,name="UsuariosGastosComunes"),
    path('OrdenPagoComun/<int:pago_id>/',OrdenPagoComun,name="OrdenPagoComun"),
    path('CapturarPagoComun/',CapturarPagoComun,name="CapturarPagoComun"),
]