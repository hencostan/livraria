from rest_framework.serializers import ModelSerializer

from core.models import Compra

from rest_framework.serializers import CharField, ModelSerializer

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        usuario = CharField(source="usuario.email", read_only=True)