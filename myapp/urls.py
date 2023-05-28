from django.urls import path
from .views import inicio, AreasAdmin, CrearAreas, GastoComun, CrearGastoComun, ListaResidentes, Foro, CrearAnuncio, ModificarAnucio, EliminarAnuncio, Registro, CrearMulta, Perfil, VerPerfil

urlpatterns = [
    path('',inicio,name="inicio"),
    path('Registro/',Registro,name="Registro"),
    path('AreasAdmin/',AreasAdmin,name="AreasAdmin"),
    path('CrearAreas/',CrearAreas,name="CrearAreas"),
    path('GastoComun/',GastoComun,name="GastoComun"),
    path('CrearGastoComun/',CrearGastoComun,name="CrearGastoComun"),
    path('ListaResidentes/',ListaResidentes,name="ListaResidentes"),
    path('Foro/',Foro,name="Foro"),
    path('CrearAnuncio/',CrearAnuncio,name="CrearAnuncio"),
    path('Modificar-Anuncio/<id>/',ModificarAnucio,name="ModificarAnucio"),
    path('Eliminar-Anuncio/<id>/',EliminarAnuncio,name="EliminarAnuncio"),
    path('CrearMulta/',CrearMulta,name="CrearMulta"),
    path('Perfil/',Perfil,name="Perfil"),
    path('VerPerfil/<int:usuario_id>/',VerPerfil,name="VerPerfil"),
]