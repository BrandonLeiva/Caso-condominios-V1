from django.urls import path
from .views import inicio, AreasAdmin, CrearAreas, GastoComun, CrearGastoComun, ListaResidentes, Foro, CrearAnuncio, ModificarAnucio, EliminarAnuncio, Registro, CrearMulta, Perfil, VerPerfil, UsuariosGastosComunes, MiGastoComun, ModificarPerfil, ReservarArea, CambiarEstadoArea, PagarGasto, CambiarEstadoComun, PagarMulta, CambiarEstado


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

    path('areas/<int:area_id>/reservar/', ReservarArea, name='ReservarArea'),
    path('CambiarEstadoArea/<int:area_id>/', CambiarEstadoArea, name='CambiarEstadoArea'),

    path('pagar/<int:pago_id>/gasto/', PagarGasto, name='PagarGasto'),
    path('CambiarEstadoComun/<int:pago_id>/', CambiarEstadoComun, name='CambiarEstadoComun'),

    path('pagar/<int:multa_id>/multa/', PagarMulta, name='PagarMulta'),
    path('CambiarEstado/<int:multa_id>/', CambiarEstado, name='CambiarEstado'),
]