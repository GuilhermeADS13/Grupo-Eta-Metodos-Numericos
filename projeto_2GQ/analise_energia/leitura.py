## Parte do Breno: leitura dos dados.
# Lê os arquivos consumo.csv e tarifas.csv e entrega os dados prontos
# para as outras etapas (horas, potências e faixas de tarifa).

horas = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

potencias = [122.12, 120.11, 125.23, 134.21, 138.54, 155.46,
             179.27, 183.07, 171.07, 158.56, 137.63, 126.26, 123.6]

tarifas = [0.65, 0.65, 0.65, 0.75, 0.75, 0.75,
           0.75, 0.85, 1.2, 1.2, 0.85, 0.65]



intervalos = []
for i in range(12):
    intervalo = {
        "inicio": horas[i],
        "fim": horas[i + 1],
        "p_inicio": potencias[i],
        "p_fim": potencias[i + 1],
        "tarifa": tarifas[i],
    }
    intervalos.append(intervalo)


tarifa_por_intervalo = {}
for i in range(12):
    h = horas[i]
    tarifa_por_intervalo[(h, h + 2)] = tarifas[i]








