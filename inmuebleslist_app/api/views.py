from rest_framework.response import Response
from rest_framework.decorators import api_view

from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer

#Funciones

@api_view()#por defecto es get
def inmueble_list(request):
    
    inmuebles = Inmueble.objects.all()
    serializer = InmuebleSerializer(inmuebles, many = True)
    
    return Response(serializer.data)


@api_view()#este es un get tambien
def inmueble_detalle(request, pk):
    inmueble = Inmueble.objects.get(pk = pk)
    serializer = InmuebleSerializer(inmueble)
    return Response(serializer.data)