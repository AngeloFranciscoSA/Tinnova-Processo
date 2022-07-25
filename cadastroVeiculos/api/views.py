from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import VeiculosSerializer
from .models import Veiculos


class VeiculosViewSet(viewsets.ModelViewSet ):
    queryset = Veiculos.objects.all()
    serializer_class = VeiculosSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'marca': ['in', 'exact'],
        'ano': ['exact'],
    }

def index(request):
    return render(request, "singlepage/index.html")
