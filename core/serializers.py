from rest_framework import serializers
from .models import Profissional, Consulta
import re
from django.utils import timezone


# --- Função auxiliar para bloquear SQL Insection ---
def validar_injecao_sql(valor):
    padroes_perigosos = [
        r"(--|\bOR\b|\bAND\b|\bDROP\b|\bSELECT\b|\bINSERT\b|\bDELETE\b)",
    ]
    for p in padroes_perigosos:
        if re.search(p, valor, flags=re.IGNORECASE):
            raise serializers.ValidationError("Entrada inválida.")
    return valor


# --- SERIALIZER DE PROFISSIONAL ---
class ProfissionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profissional
        fields = "__all__"

    # Sanitização + validação de cada campo
    def validate_nome_social(self, valor):
        valor = valor.strip()

        if len(valor) < 2:
            raise serializers.ValidationError("O nome social é muito curto.")

        if len(valor) > 255:
            raise serializers.ValidationError("O nome social excede o limite permitido.")

        validar_injecao_sql(valor)
        return valor

    def validate_profissao(self, valor):
        valor = valor.strip()

        if len(valor) < 2:
            raise serializers.ValidationError("A profissão é muito curta.")

        if len(valor) > 100:
            raise serializers.ValidationError("A profissão excede o limite permitido.")

        validar_injecao_sql(valor)
        return valor

    def validate_endereco(self, valor):
        valor = valor.strip()

        if len(valor) < 5:
            raise serializers.ValidationError("O endereço é muito curto.")

        if len(valor) > 255:
            raise serializers.ValidationError("O endereço excede o limite permitido.")

        validar_injecao_sql(valor)
        return valor

    def validate_contato(self, valor):
        valor = valor.strip()

        # Estabeleci um limite de contatos entre 5 a 100. É suficiente.
        if len(valor) < 5:
            raise serializers.ValidationError("O contato é muito curto.")

        if len(valor) > 100:
            raise serializers.ValidationError("O contato excede o limite permitido.")

        validar_injecao_sql(valor)
        return valor


# --- SERIALIZER DE CONSULTA ---
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = "__all__"

    def validate_data(self, valor):
        if valor < timezone.now():
            raise serializers.ValidationError("A data da consulta não pode ser no passado.")
        return valor

    def validate_profissional(self, valor):
        if not isinstance(valor.id, int):
            raise serializers.ValidationError("ID do profissional inválido.")
        return valor
