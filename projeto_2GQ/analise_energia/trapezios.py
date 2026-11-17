from math import isfinite
from numbers import Real


def calcular_energias(medicoes):
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
