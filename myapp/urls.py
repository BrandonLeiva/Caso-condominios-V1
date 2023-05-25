from django.urls import path
from .views import inicio, AreasAdmin, CrearAreas, GastoComun, CrearGastoComun, ListaResidentes, Foro, CrearAnuncio, ModificarAnucio, EliminarAnuncio

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AreasAdmin/',AreasAdmin,name="AreasAdmin"),
    path('CrearAreas/',CrearAreas,name="CrearAreas"),
    path('GastoComun/',GastoComun,name="GastoComun"),
    path('CrearGastoComun/',CrearGastoComun,name="CrearGastoComun"),
    path('ListaResidentes/',ListaResidentes,name="ListaResidentes"),
    path('Foro/',Foro,name="Foro"),
    path('CrearAnuncio/',CrearAnuncio,name="CrearAnuncio"),
    path('Modificar-Anuncio/<id>/',ModificarAnucio,name="ModificarAnucio"),
    path('Eliminar-Anuncio/<id>/',EliminarAnuncio,name="EliminarAnuncio"),
]