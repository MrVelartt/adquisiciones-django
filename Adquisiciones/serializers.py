from rest_framework import serializers
from reversion.models import Version
from .models import Acquisition

class AcquisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acquisition
        fields = '__all__'

class VersionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fecha = serializers.DateTimeField(source='revision.date_created')
    usuario = serializers.SerializerMethodField()
    comentario = serializers.CharField(source='revision.get_comment', allow_blank=True)
    datos = serializers.SerializerMethodField()

    def get_usuario(self, obj: Version):
        user = obj.revision.user
        return user.username if user else None

    def get_datos(self, obj: Version):
        # field_dict devuelve un dict con todos los campos y su valor en esa versión
        return obj.field_dict