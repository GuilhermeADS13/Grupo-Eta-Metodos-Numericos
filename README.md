#  GRUPO ETA - MÉTODOS NUMÉRICOS

> Resolução numérica em Python para determinação da corrente elétrica em um circuito com dispositivo não-linear.

---

##  Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Descrição do Problema](#-descrição-do-problema)
- [Modelagem Matemática](#-modelagem-matemática)
- [Métodos Numéricos Implementados](#-métodos-numéricos-implementados)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar](#-como-executar)
- [Integrantes](#-integrantes)

---

## 📖 Sobre o Projeto

Este projeto foi desenvolvido em **Python** para a disciplina de **Métodos Numéricos** pelo **Grupo Eta**. O objetivo principal é aplicar e comparar algoritmos numéricos de busca de raízes de equações não-lineares resultantes da análise de circuitos elétricos.

---

##  Descrição do Problema

Considere o circuito elétrico formado por:
- Uma fonte de tensão $E$;
- Um resistor de resistência $R$;
- Um dispositivo não-linear cuja relação entre tensão e corrente é dada por $v = g(i)$.

### Parâmetros do Circuito:
- **Fonte de Tensão ($E$):** $10\text{ V}$
- **Resistência ($R$):** $2\ \Omega$
- **Relação Tensão-Corrente:** $g(i) = i^3$

---

##  Modelagem Matemática

Aplicando a **Lei das Tensões de Kirchhoff** (LTK) ao circuito:

$$E - R \cdot i - g(i) = 0$$

Substituindo os valores do problema ($E = 10$, $R = 2$ e $g(i) = i^3$):

$$10 - 2i - i^3 = 0$$

Reorganizando para encontrar a raiz $f(i) = 0$:

$$f(i) = i^3 + 2i - 10 = 0$$

O objetivo numérico é determinar o valor aproximado da corrente $i$ (em Ampères) que satisfaz esta equação.

---

##  Métodos Numéricos Implementados

Para resolver a equação $f(i) = 0$, foram implementados em Python os seguintes métodos:

1. **Método da Bisseção**
2. **Método da Falsa Posição**
3. **Método de Newton-Raphson**
4. **Método das Secantes**

---

##  Tecnologias Utilizadas

- **Linguagem:** Python 3.x


---

## 🚀 Como Executar

### Pré-requisitos
Ter o **Python 3.x** instalado.
