## Parte do Breno: leitura dos dados.
# Guarda os dados do problema (potência medida a cada 2 h e tarifa de cada
# intervalo), digitados a partir de consumo.csv e tarifas.csv do enunciado,
# e entrega os dados prontos para as outras etapas (horas, potências e
# faixas de tarifa).

horas = []
potencias = []
f = open("consumo.csv")
f.readline()  
for linha in f:
    hora, potencia = linha.strip().split(",")
    horas.append(int(hora))
    potencias.append(float(potencia))
f.close()

tarifas = []
f = open("tarifas.csv")
f.readline()  
for linha in f:
    inicio, fim, tarifa = linha.strip().split(",")
    tarifas.append(float(tarifa))
f.close()



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








