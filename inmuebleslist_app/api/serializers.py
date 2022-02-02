from rest_framework import serializers
from inmuebleslist_app.models import Inmueble


#clases

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    description = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()