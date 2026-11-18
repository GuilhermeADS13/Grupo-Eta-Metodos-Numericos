## Parte da Manuela: programa principal e integração.
# Chama as funções de cada etapa (leitura, energia, custo, comparação
# e economia) na ordem certa e mostra os resultados de todos os itens.

from projeto_2GQ.analise_energia.leitura import horas, potencias, tarifas
from projeto_2GQ.analise_energia.trapezios import calcular_energias
from projeto_2GQ.analise_energia.custo import calcular_custos

medicoes = list(zip(horas, potencias))
energias, energia_total = calcular_energias(medicoes)

# Item (b) - custo da energia consumida
custos, custo_total = calcular_custos(energias, tarifas)

print("Item (b) - Custo da energia por intervalo")
print("Intervalo | Energia (kWh) | Tarifa (R$/kWh) | Custo (R$)")
for i in range(len(custos)):
    print(f"{horas[i]:02d}-{horas[i + 1]:02d}h    | {energias[i]:13.2f} | {tarifas[i]:15.2f} | {custos[i]:10.2f}")
print(f"Custo total: R$ {custo_total:.2f}")

