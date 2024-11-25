from rest_framework.serializers import ModelSerializer

from core.models import Compra, ItensCompra

from rest_framework.serializers import CharField, ModelSerializer

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
        depth = 1

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        usuario = CharField(source="usuario.email", read_only=True)
        itens = ItensCompraSerializer(many=True, read_only=True)