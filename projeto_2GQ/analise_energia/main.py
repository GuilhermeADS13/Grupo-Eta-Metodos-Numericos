## Parte da Manuela: programa principal e integração.
# Chama as funções de cada etapa (leitura, energia, custo, comparação
# e economia) na ordem certa e mostra os resultados de todos os itens.

from projeto_2GQ.analise_energia.leitura import horas, potencias, tarifas
from projeto_2GQ.analise_energia.trapezios import calcular_energias
from projeto_2GQ.analise_energia.custo import calcular_custos
from projeto_2GQ.analise_energia.comparacao import comparar_periodos

try:
    from projeto_2GQ.analise_energia.economia import calcular_economias
except ImportError:
    calcular_economias = None


def nome_intervalo(i):
    return f"{horas[i]:02d}-{horas[i + 1]:02d}h"


def linha():
    print("-" * 62)


def mostrar_item_a(energias, energia_total):
    print("Item (a) - Energia total consumida em 24 h (regra dos trapézios)")
    linha()
    print("Intervalo | P inicial (kW) | P final (kW) | Energia (kWh)")
    for i in range(len(energias)):
        print(f"{nome_intervalo(i)}    | {potencias[i]:14.2f} | {potencias[i + 1]:12.2f} | {energias[i]:13.2f}")
    print(f"Energia total: {energia_total:.2f} kWh")
    print()


def mostrar_item_b(energias, custos, custo_total):
    print("Item (b) - Custo da energia consumida")
    linha()
    print("Intervalo | Energia (kWh) | Tarifa (R$/kWh) | Custo (R$)")
    for i in range(len(custos)):
        print(f"{nome_intervalo(i)}    | {energias[i]:13.2f} | {tarifas[i]:15.2f} | {custos[i]:10.2f}")
    print(f"Custo total: R$ {custo_total:.2f}")
    print()


def mostrar_item_c(energias):
    e1, e2, maior, dif_real = comparar_periodos(energias)

    print("Item (c) - Primeiras 12 h x últimas 12 h")
    linha()
    print(f"Primeiras 12 h (00-12h): {e1:.2f} kWh")
    print(f"Últimas 12 h (12-24h):   {e2:.2f} kWh")
    print(f"Período com maior consumo: {maior}")
    print(f"Diferença relativa (referência: primeiras 12 h): {dif_real:.2f}%")
    print()


def mostrar_item_d(energias):
    print("Item (d) - Redução de 10% em um intervalo de 2 h")
    linha()

    if calcular_economias is None:
        print("Pendente: a função calcular_economias ainda não está em economia.py.")
        print()
        return

    economias, indice_maior, economia_mensal = calcular_economias(energias, tarifas)

    print("Intervalo | Energia (kWh) | Tarifa (R$/kWh) | Economia/dia (R$)")
    for i in range(len(economias)):
        marca = "  <- maior" if i == indice_maior else ""
        print(f"{nome_intervalo(i)}    | {energias[i]:13.2f} | {tarifas[i]:15.2f} | {economias[i]:17.2f}{marca}")
    print(f"Intervalo com maior economia: {nome_intervalo(indice_maior)}")
    print(f"Economia diária: R$ {economias[indice_maior]:.2f}")
    print(f"Economia em 30 dias: R$ {economia_mensal:.2f}")
    print()


def main():
    print("Análise do Consumo de Energia de um Data Center - Grupo Eta")
    print("=" * 62)
    print()

    medicoes = list(zip(horas, potencias))
    energias, energia_total = calcular_energias(medicoes)

    custos, custo_total = calcular_custos(energias, tarifas)

    mostrar_item_a(energias, energia_total)
    mostrar_item_b(energias, custos, custo_total)
    mostrar_item_c(energias)
    mostrar_item_d(energias)


if __name__ == "__main__":
    main()
