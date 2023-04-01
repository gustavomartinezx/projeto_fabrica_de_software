from django.shortcuts import render
from rest_framework import viewsets
from .models import Loja
from .models import Album
from .models import Cliente
from .serializers import ClienteSerializer
from .serializers import AlbumSerializer
from .serializers import LojaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
