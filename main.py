from problema import f, f_linha, phi, eps1, eps2, kmax
from bissecao import bissecao
from newton_raphson import newton_raphson
from  ponto_fixo import ponto_fixo

print("Método da Bisseção:")
raiz, iteracoes = bissecao(f, 1, 2, eps1, eps2, kmax)
print("Bissecao: i =", raiz, "em", iteracoes, "iteracoes" "\n")
print("Método de Newton-Raphson:" "\n")
raiz, iteracoes = newton_raphson(f, f_linha, 1, eps1, eps2, kmax)
print("Newton-Raphson: i =", raiz, "em", iteracoes, "iteracoes" "\n")
print("Método do Ponto Fixo:" "\n")
raiz, iteracoes = ponto_fixo(phi, f, 1, eps1, eps2, kmax)
print("Ponto Fixo: i =", raiz, "em", iteracoes, "iteracoes" "\n")
