from django.shortcuts import render

from rest_framework import generics
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer

class ProfissionalListCreate(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ProfissionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ConsultaListCreate(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
