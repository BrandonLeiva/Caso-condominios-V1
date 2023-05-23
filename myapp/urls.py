from django.urls import path
from .views import inicio, AreasAdmin, CrearAreas, CrearGastoComun, GastoComun, ListaResidentes

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AreasAdmin/',AreasAdmin,name="AreasAdmin"),
    path('CrearAreas/',CrearAreas,name="CrearAreas"),
    path('PagarGastoComun/',CrearGastoComun,name="CrearGastoComun"),
    path('GastoComun/',GastoComun,name="GastoComun"),
    path('ListaResidentes/',ListaResidentes,name="ListaResidentes"),
]