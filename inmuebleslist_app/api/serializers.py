from rest_framework import serializers
from inmuebleslist_app.models import Inmueble


#clases

class InmuebleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inmueble
        fields = "__all__"        
        #fields = ['pais','active','direccion','description']
        #exclude = ['id']
        
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("La direccion y el pais deben ser diferentes")
        else:
            data

    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("La url de la imagen es demasiado corta")
        else:
            data


# def column_longitud(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("El valor es demasiado corto")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     description = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     #para el post
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.description = validated_data.get('description', instance.description)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #Esta es una funcion propia del framework, la estamos sobreescribiendo
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError("La direccion y el pais deben ser diferentes")
#         else:
#             data
    
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("La url de la imagen es demasiado corta")
#         else:
#             data