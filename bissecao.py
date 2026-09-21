#implementa a bisseção aqui


def bissecao(f, a, b, eps1, eps2, kmax):
    if abs(f(a)) < eps1:
        return a, 0

    if abs(f(b)) < eps1:
        return b, 0

    for k in range(1, kmax + 1):
        i = (a + b)/2 #ponto medio do intervalo

        print("iteracao" , k ,"i =" , i)

        if abs(f(i)) < eps1 or abs(b - a) < eps2:
            return i, k

        if f(a)*f(i) > 0: #mesmo sinal, a raiz esta na outra metade
            a = i
        else:
            b = i

    return (a + b)/2, kmax
