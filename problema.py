import math

#Problema inicial
#Equação dada no projeto: E - R * i - g(i) = 0
#Sendo e = 10, r = 2, g(i) = i**3

def f(i):
    return 10 - 2 * i - (i ** 3)



def f_linha(i):
    return -2 - 3 * (i ** 2)


<<<<<<< HEAD
=======

def phi(i): 
    return (10 - 2 * i) ** (1/3)


>>>>>>> 1d16d6362284d6409ecc8844806087c571341d02
eps1 = 1e-4
eps2 = 1e-4
kmax = 50
