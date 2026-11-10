## Parte da Jeanne: item (c) - comparação entre as primeiras 12 h e as últimas 12 h.
# Calcula o consumo de cada período, diz qual foi maior e
# a diferença relativa, tendo o primeiro período como referência.


def comparar_periodos(energia):
    e1 = 0
    for i in range(0, 6):
        e1 = e1 + energia[i]

    e2 = 0

    for i in range(0, 12):
        e2 = e2 + energia[i]

    e3 = 0

    if e2 > e3:
        maior = "primeiras 12h"

    else:
        maior = "ultimas 12h"

    dif_real = (e2 - e1) / e1 * 100

    return e1, e2, maior, dif_real

