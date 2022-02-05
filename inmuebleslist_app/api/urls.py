from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inmuebleslist_app.api.views import (
    #inmueble_list, 
    #inmueble_detalle
    InmuebleListAV,
    InmuebleDetalleAV,
    EmpresaAV,
    EmpresaDetalleAV,
    ComentarioDetail,
    ComentarioList,
    ComentarioCreate,
    EmpresaVS,
)

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename='empresa')

urlpatterns = [
    path('inmueble/list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('inmueble/<int:pk>/', InmuebleDetalleAV.as_view(), name='inmueble-detail'),
    
    path('', include(router.urls)),
    # path('empresa/', EmpresaAV.as_view(), name='empresa'),    
    # path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),    
        
    path('inmueble/<int:pk>/comentario-create', ComentarioCreate.as_view(), name='comentario-create'),
    path('inmueble/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),    
    path('inmueble/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail'),
]