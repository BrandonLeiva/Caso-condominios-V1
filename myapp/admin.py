from django.contrib import admin
from.models import status, PagoComun, AreaComun, Anuncio, Multa

# Register your models here.

admin.site.register(status)
admin.site.register(PagoComun)
admin.site.register(AreaComun)
admin.site.register(Anuncio)
admin.site.register(Multa)