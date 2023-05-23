from django.urls import path
from .views import inicio, AreasAdmin, CrearAreas, CrearGastoComun

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AreasAdmin/',AreasAdmin,name="AreasAdmin"),
    path('CrearAreas/',CrearAreas,name="CrearAreas"),
    path('PagarGastoComun/',CrearGastoComun,name="CrearGastoComun"),
]