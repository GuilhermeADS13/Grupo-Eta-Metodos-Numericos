## Parte do Guilherme: item (b) - custo da energia consumida.
# Multiplica a energia de cada intervalo pela tarifa da faixa
# correspondente e soma o custo total, em R$.
# O calculo e feito intervalo a intervalo, nunca com tarifa media.


def calcular_custos(energias, tarifas):
    if len(energias) != len(tarifas):
        raise ValueError("Cada intervalo de energia precisa de uma tarifa.")

    custos = []
    custo_total = 0
    for i in range(len(energias)):
        custo = energias[i] * tarifas[i]
        custos.append(custo)
        custo_total = custo_total + custo

    return custos, custo_total
