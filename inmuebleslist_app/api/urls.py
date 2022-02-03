from django.urls import path
from inmuebleslist_app.api.views import (
    #inmueble_list, 
    #inmueble_detalle
    InmuebleListAV,
    InmuebleDetalleAV,
    EmpresaAV,
    EmpresaDetalleAV,
)

urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:pk>/', InmuebleDetalleAV.as_view(), name='inmueble-detail'),
    path('empresa/', EmpresaAV.as_view(), name='empresa'),    
    path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),    
]