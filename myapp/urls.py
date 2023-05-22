from django.urls import path
from .views import inicio, AreasAdmin

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AreasAdmin/',AreasAdmin,name="AreasAdmin"),
]