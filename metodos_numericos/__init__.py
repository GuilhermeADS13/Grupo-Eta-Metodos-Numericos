"""Metodos numericos para determinacao de raizes de equacoes nao-lineares.

Implementado pelo Grupo Eta para a disciplina de Metodos Numericos.
Os tres metodos sao genericos: recebem a funcao do problema por parametro.
"""

from .bissecao import bissecao
from .newton_raphson import newton_raphson
from .ponto_fixo import ponto_fixo

__all__ = ["bissecao", "newton_raphson", "ponto_fixo"]
