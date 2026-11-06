# GRUPO ETA - MÉTODOS NUMÉRICOS

> Resolução numérica em Python para determinação da corrente elétrica em um circuito com dispositivo não-linear.

---

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Descrição do Problema](#descrição-do-problema)
- [Modelagem Matemática](#modelagem-matemática)
- [Métodos Numéricos Implementados](#métodos-numéricos-implementados)
- [Critério de Parada e Precisão](#critério-de-parada-e-precisão)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Instalação](#instalação)
- [Como Executar](#como-executar)

---

## Sobre o Projeto

Este projeto foi desenvolvido em **Python** para a disciplina de **Métodos Numéricos** pelo **Grupo Eta**. O objetivo é aplicar e comparar algoritmos numéricos de busca de raízes de equações não-lineares resultantes da análise de circuitos elétricos.

Os métodos foram implementados pelo próprio grupo, sem utilizar funções prontas de bibliotecas para determinação de raízes.

---

## Descrição do Problema

Considere o circuito elétrico formado por:
- Uma fonte de tensão $E$;
- Um resistor de resistência $R$;
- Um dispositivo não-linear cuja relação entre tensão e corrente é dada por $v = g(i)$.

### Parâmetros do Circuito

- **Fonte de Tensão ($E$):** $10\text{ V}$
- **Resistência ($R$):** $2\ \Omega$
- **Relação Tensão-Corrente:** $g(i) = i^3$

---

## Modelagem Matemática

Aplicando a **Lei das Tensões de Kirchhoff** (LTK) ao circuito:

$$E - R \cdot i - g(i) = 0$$

Substituindo os valores do problema ($E = 10$, $R = 2$ e $g(i) = i^3$), chega-se à forma $f(i) = 0$:

$$f(i) = 10 - 2i - i^3 = 0$$

O objetivo numérico é determinar o valor aproximado da corrente $i$ (em ampères) que satisfaz esta equação.

Como $f(1) = 7 > 0$ e $f(2) = -2 < 0$, existe pelo menos uma raiz no intervalo $[1, 2]$.

---

## Métodos Numéricos Implementados

| Método | Arquivo | Precisa de | Convergência |
|---|---|---|---|
| **Bisseção** | `metodos_numericos/bissecao.py` | intervalo $[a, b]$ com sinais opostos | linear, sempre converge |
| **Newton-Raphson** | `metodos_numericos/newton_raphson.py` | $f'(i) = -2 - 3i^2$ | quadrática, pode divergir |
| **Ponto Fixo** | `metodos_numericos/ponto_fixo.py` | $\varphi(i) = \sqrt[3]{10 - 2i}$ | linear, exige $\lvert \varphi'(i) \rvert < 1$ |

Os três métodos são **genéricos**: recebem a função do problema por parâmetro e retornam `(raiz, iteracoes)`.

### Resultados

| Método | Raiz (A) | Iterações | $\lvert f(i) \rvert$ |
|---|---|---|---|
| Bisseção | 1,847412 | 12 | $8{,}48 \times 10^{-5}$ |
| Newton-Raphson | 1,847419 | 5 | $5{,}73 \times 10^{-10}$ |
| Ponto Fixo | 1,847428 | 7 | $1{,}05 \times 10^{-4}$ |

---

## Critério de Parada e Precisão

Os três métodos usam o mesmo critério, para que a comparação seja justa:

| Parâmetro | Valor | Para quando |
|---|---|---|
| `eps1` | $10^{-4}$ | $\lvert f(i) \rvert < eps1$ — o valor já está perto o bastante de zero |
| `eps2` | $10^{-4}$ | a variação entre dois passos é menor que `eps2` — o método parou de avançar |
| `kmax` | 50 | limite de iterações, segurança contra não-convergência |

**Justificativa da precisão.** A corrente procurada é da ordem de 1,8 A. Uma tolerância de $10^{-4}$ garante quatro casas decimais, ou seja, erro abaixo de 0,1 mA — precisão muito acima da de qualquer instrumento de bancada. Não há ganho prático em exigir mais.

**Por que dois critérios.** Cada um cobre uma falha do outro. Perto de uma raiz onde a função é achatada, $\lvert f(i) \rvert$ fica pequeno enquanto $i$ ainda muda bastante; já em uma convergência lenta, $i$ quase para de variar enquanto $\lvert f(i) \rvert$ continua grande. Ligados por *ou*, o método para assim que qualquer uma das garantias for atingida.

**Por que `kmax`.** Nem todo método converge: o ponto fixo diverge se $\lvert \varphi'(i) \rvert > 1$ e o Newton-Raphson pode oscilar com um chute ruim. Sem esse limite, o programa entraria em laço infinito. O valor 50 é folgado — o método mais lento precisou de 12 iterações.

---

## Estrutura do Repositório

```text
metodos_numericos/        pacote com os métodos (genéricos, instalável via pip)
    __init__.py
    bissecao.py
    newton_raphson.py
    ponto_fixo.py
problema.py               definição do circuito: f, f', phi e os parâmetros
analise.ipynb             notebook que importa o pacote e resolve o problema
main.py                   script equivalente, para rodar pelo terminal
pyproject.toml            configuração do pacote
```

A separação é proposital: o **pacote** não sabe qual é a equação, ele recebe a função por parâmetro. Quem descreve o circuito é o `problema.py`. Assim os métodos servem para qualquer outra equação.

---

## Instalação

### Pré-requisitos

- **Python 3.9** ou superior

### Instalando o pacote

Na raiz do repositório:

```bash
pip install .
```

Para desenvolvimento, instale em modo editável (as alterações no código passam a valer sem reinstalar):

```bash
pip install -e .
```

Para abrir o notebook, instale também o Jupyter:

```bash
pip install jupyter
```

---

## Como Executar

### Pelo notebook (recomendado)

```bash
jupyter notebook analise.ipynb
```

O notebook importa as funções do pacote, aplica os três métodos ao problema e mostra os resultados. Execute a partir da raiz do repositório, porque ele importa o `problema.py`.

### Pelo terminal

```bash
python main.py
```

Saída esperada:

```text
Bissecao: i = 1.847412109375 em 12 iteracoes
Newton-Raphson: i = 1.8474190378795425 em 5 iteracoes
Ponto Fixo: i = 1.8474276309404878 em 7 iteracoes
```

### Usando o pacote em outro projeto

Depois de instalado, os métodos podem ser usados com qualquer equação:

```python
from metodos_numericos import bissecao

f = lambda x: x**2 - 2
raiz, iteracoes = bissecao(f, 1, 2, 1e-4, 1e-4, 50)
```
