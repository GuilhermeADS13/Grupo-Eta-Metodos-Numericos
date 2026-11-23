# Projeto 2GQ: Consumo de Energia de um Data Center

**Problema 4 - Grupo Eta**

A potência elétrica de um data center foi medida a cada 2 horas ao longo de 24 horas (13 medições, de 0 h a 24 h). A energia é cobrada por faixa de horário, com uma tarifa diferente para cada um dos 12 intervalos de 2 horas.

- **(a)** energia total consumida no dia, pela regra dos trapézios;
- **(b)** custo total, intervalo a intervalo, com a tarifa de cada faixa;
- **(c)** consumo das primeiras 12 h e das últimas 12 h e a diferença relativa entre eles;
- **(d)** intervalo em que uma redução de 10% no consumo gera a maior economia, e a economia em 30 dias.

## Estrutura

```text
README.md
pyproject.toml                configuração do pacote (pip install .)
projeto_2GQ/
    analise_energia.ipynb     notebook que importa o pacote e resolve os itens
    analise_energia/
        leitura.py            dados de potência e tarifas
        trapezios.py          item (a)
        custo.py              item (b)
        comparacao.py         item (c)
        economia.py           item (d)
        main.py               programa principal
```

## Instalação

Na raiz do repositório:

```bash
pip install .
```

Rode de novo depois de cada `git pull`.

## Como executar

Pelo notebook:

```bash
jupyter notebook projeto_2GQ/analise_energia.ipynb
```

Pelo terminal, a partir da raiz do repositório:

```bash
python -m projeto_2GQ.analise_energia.main
```

## Resultados

| Item | Resultado |
|---|---|
| (a) Energia total | 3 504,54 kWh |
| (b) Custo total | R$ 2 872,14 |
| (c) Últimas 12 h × primeiras 12 h | 1 856,05 kWh × 1 648,49 kWh (+12,59%) |
| (d) Melhor intervalo para reduzir 10% | 16–18 h: R$ 39,56/dia, R$ 1 186,67 em 30 dias |

## Integrantes

Breno, Guilherme, Mirna, Manuela, Allan e Jeanne.
