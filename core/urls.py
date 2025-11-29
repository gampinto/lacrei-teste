from django.urls import path
from .views import (
    ProfissionalListCreate, ProfissionalRetrieveUpdateDestroy,
    ConsultaListCreate, ConsultaRetrieveUpdateDestroy
)

urlpatterns = [
    path('profissionais/', ProfissionalListCreate.as_view(), name='profissional-list'),
    path('profissionais/<int:pk>/', ProfissionalRetrieveUpdateDestroy.as_view(), name='profissional-detail'),

    path('consultas/', ConsultaListCreate.as_view(), name='consulta-list'),
    path('consultas/<int:pk>/', ConsultaRetrieveUpdateDestroy.as_view(), name='consulta-detail'),
]
