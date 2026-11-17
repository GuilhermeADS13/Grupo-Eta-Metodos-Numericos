"""Integração numérica pela regra dos trapézios."""

from math import isfinite
from numbers import Real


def calcular_energias(medicoes):
    """Retorna (energias_por_intervalo, energia_total), ambos em kWh.

    Recebe um iterável de pares (hora, potencia_kw), com pelo menos duas
    medições. Os valores devem ser números reais finitos e os horários devem
    ser estritamente crescentes. Entradas inválidas geram ValueError.

    Energia é a integral da potência em relação ao tempo. Para medições
    discretas, a regra dos trapézios aproxima essa integral assumindo que a
    potência varia linearmente entre medições consecutivas. Variações dentro
    de um intervalo podem escapar a essa aproximação. Somar as potências
    ainda dá um valor em kW. Multiplicar a potência média pela duração em
    horas dá a energia em kWh.
    """
    energias = []
    hora_anterior = None
    potencia_anterior = None

    for indice, medicao in enumerate(medicoes, start=1):
        try:
            hora, potencia = medicao
        except (TypeError, ValueError) as erro:
            raise ValueError(f"Medição {indice} deve ser um par (hora, potência).") from erro

        if any(
            isinstance(valor, bool) or not isinstance(valor, Real) or not isfinite(valor)
            for valor in (hora, potencia)
        ):
            raise ValueError(f"Hora e potência da medição {indice} devem ser números reais finitos.")

        if hora_anterior is not None:
            duracao = hora - hora_anterior
            if duracao <= 0:
                raise ValueError("Os horários devem estar em ordem estritamente crescente.")
            potencia_media = (potencia_anterior + potencia) / 2
            energias.append(potencia_media * duracao)

        hora_anterior = hora
        potencia_anterior = potencia

    if not energias:
        raise ValueError("São necessárias pelo menos duas medições.")

    return energias, sum(energias)
