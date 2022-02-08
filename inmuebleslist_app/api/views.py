from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from inmuebleslist_app.models import (
    Inmueble, Empresa, Comentario
)

from inmuebleslist_app.api.serializers import (
    InmuebleSerializer, EmpresaSerializer, ComentarioSerializer
)

class ComentarioCreate(generics.CreateAPIView):    
    serializer_class = ComentarioSerializer
    
    #Con esto devolvemos el comentario creado al cliente
    def get_queryset(self):
        return Comentario.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        edificacion = Inmueble.objects.get(pk = pk)
        
        user = self.request.user
        comentario_queryset = Comentario.objects.filter(inmueble=edificacion, 
                                                        comentario_user=user)
        if comentario_queryset.exists():
            raise ValidationError("El usuario ya escribio un comentario para este inmueble")
        
        serializer.save(inmueble = edificacion)
    

class ComentarioList(generics.ListCreateAPIView):
    #queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(inmueble = pk)
        
    
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


# class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class ComentarioDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class EmpresaVS(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Empresa.objects.all()    
    serializer_class = EmpresaSerializer
    

# class EmpresaVS(viewsets.ViewSet):
#     #list viene de ViewSet, la estamos sobreescribiendo
#     def list(self, request):
#         queryset = Empresa.objects.all()
#         serializer = EmpresaSerializer(queryset, many = True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk = None):
#         queryset = Empresa.objects.all()
#         inmueblelist = get_object_or_404(queryset, pk = pk)
#         serializer = EmpresaSerializer(inmueblelist)
#         return Response(serializer.data)
    
#     def create(slef, request):
#         serializer = EmpresaSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors, status = 
#                      status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'error':'Empresa no encontrada'},
#                             status=status.HTTP_404_NOT_FOUND)
            
#         serializer =  EmpresaSerializer(empresa, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors, status=
#                      status.HTTP_400_BAD_REQUEST)
            
#     def destroy(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'error':'Empresa no encontrada'}, 
#                             status=status.HTTP_404_NOT_FOUND)
            
#         empresa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

class EmpresaAV(APIView):
    
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        #data que hay que convertir a un formato python
        serializer = EmpresaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EmpresaDetalleAV(APIView):
    
    def get(self, request, pk):
        try:#Buscando empresa
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'Error':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
       
        serializer = EmpresaSerializer(Empresa, context={'request':request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'Error':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data, context={'request':request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk = pk)
        except Empresa.DoesNotExist:
            return Response( {'error': 'Empresa no encontrada'}, status = status.HTTP_404_NOT_FOUND)
                
        empresa.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  


class InmuebleListAV(APIView):
    
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InmuebleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class InmuebleDetalleAV(APIView):
    
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk = pk)
        except Inmueble.DoesNotExist:
            return Response( {'error': 'Inmueble no encontrado'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    
    def put(self, request,pk):
        try:
            inmueble = Inmueble.objects.get(pk = pk)
        except Inmueble.DoesNotExist:
            return Response( {'error': 'Inmueble no encontrado'}, status = status.HTTP_404_NOT_FOUND)

        serializer = InmuebleSerializer(inmueble, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk = pk)
        except Inmueble.DoesNotExist:
            return Response( {'error': 'Inmueble no encontrado'}, status = status.HTTP_404_NOT_FOUND)
        
        inmueble.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#Funciones

""" @api_view(['GET', 'POST'])
def inmueble_list(request):
    
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many = True)
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        de_serializer = InmuebleSerializer(data = request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detalle(request, pk):
    
    if request.method == 'GET':
        try:
            inmueble = Inmueble.objects.get(pk = pk)
            serializer = InmuebleSerializer(inmueble)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response( {'Error' : 'El inmueble no existe'}, 
                            status = status.HTTP_404_NOT_FOUND )
        
    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk = pk)
        de_serializer = InmuebleSerializer(inmueble, data = request.data)
        
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        try:
            inmueble = Inmueble.objects.get(pk = pk)
            inmueble.delete()
        except Inmueble.DoesNotExist:
            return Response({'Error' : 'El inmueble no existe'}, 
                            status = status.HTTP_404_NOT_FOUND)
        
        return Response(status = status.HTTP_204_NO_CONTENT) """