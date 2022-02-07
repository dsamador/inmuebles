from rest_framework import serializers
from inmuebleslist_app.models import Inmueble, Empresa, Comentario


#clases
class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comentario
        exclude = ['inmueble']


class InmuebleSerializer(serializers.ModelSerializer):    
    comentarios = ComentarioSerializer(many=True, read_only=True)    
    class Meta:
        model = Inmueble
        fields = "__all__"        
        #fields = ['pais','active','direccion','description']
        #exclude = ['id']
        
        
class EmpresaSerializer(serializers.ModelSerializer):
    #con esto pedimos todos los registros de Inmuebles por empresa
    inmueblelist = InmuebleSerializer(many = True, read_only=True)
    
    #Como el anterior pero toma solo el dato de la funcion str
    #inmueblelist = serializers.StringRelatedField(many= True)
    
    #Devuelve los id de los inmubles que tiene la empresa
    #inmueblelist = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
    
    #con esto devolvemos el endpoint de cada inmueble
    # inmueblelist = serializers.HyperlinkedRelatedField(
    #     many = True, 
    #     read_only = True,
    #     view_name = 'inmueble-detalle'#nombre de la url en el urls.py
    #     )
    
    class Meta:
        model = Empresa 
        fields = "__all__"

        
        
    
    #Campo calculado, no viene del modelo
    #longitud_direccion = serializers.SerializerMethodField()
        
    # def get_longitud_direccion(self, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres
        
    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError("La direccion y el pais deben ser diferentes")
    #     else:
    #         data

    # def validate_imagen(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError("La url de la imagen es demasiado corta")
    #     else:
    #         data


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