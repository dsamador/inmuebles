from django.contrib           import admin
from inmuebleslist_app.models import (
    Inmueble, Empresa
)


# Register your models here.


admin.site.register(Inmueble)
admin.site.register(Empresa)