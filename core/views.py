from django.shortcuts import render

from rest_framework import generics
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer

def allow_if_api_key(request):
    """Retorna True se E APENAS SE a requisição veio com API Key válida."""
    return getattr(request, "is_internal_api", False)
class ProfissionalListCreate(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

def get_permissions(self):
        if allow_if_api_key(self.request):
            return []
        return super().get_permissions()

class ProfissionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

def get_permissions(self):
        if allow_if_api_key(self.request):
            return []
        return super().get_permissions()

class ConsultaListCreate(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    
    def get_permissions(self):
        if allow_if_api_key(self.request):
            return []
        return super().get_permissions()

class ConsultaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    
def get_permissions(self):
        if allow_if_api_key(self.request):
            return []
        return super().get_permissions()