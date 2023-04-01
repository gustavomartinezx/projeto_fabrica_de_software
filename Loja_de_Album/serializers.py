from rest_framework import serializers
from .models import Cliente
from .models import Loja
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'nome', 'artista', 'lancamento', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id', 'nome', 'endereco', 'tel_para_contato']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nome', 'endereco_de_residencia', 'email']