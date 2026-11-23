## Parte do Allan: item (d) - redução de 10% em um intervalo de 2 h.
# Descobre qual intervalo gera a maior economia financeira
# e estima a economia em um mês de 30 dias.


def calcular_economias(energias, tarifas, reducao=0.10):
    if len(energias) != len(tarifas):
        raise ValueError("Cada intervalo de energia precisa de uma tarifa.")

    economias = []
    for i in range(len(energias)):
        economia = reducao * energias[i] * tarifas[i]
        economias.append(economia)

    return economias


def melhor_intervalo(economias, dias=30):
    indice = 0
    for i in range(1, len(economias)):
        if economias[i] > economias[indice]:
            indice = i

    economia_diaria = economias[indice]
    economia_mensal = economia_diaria * dias

    return indice, economia_diaria, economia_mensal
