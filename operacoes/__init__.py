def soma(n1=0, n2=0):
    r = n1 + n2
    return r


def subtracao(n1=0, n2=0):
    r = n1 - n2
    return r


def multiplicacao(n1=1, n2=1):
    r = n1 * n2
    return r


def divisao(n1=1, n2=1):
    try:
        r = n1 / n2
    except ZeroDivisionError:
        n2 = 1
        print ('\nNao é possivel a efetuaçao da operacao DIVISAO com denominador = 0\n'
               'O denominador foi aterado = 1. ')
    finally:
        r = n1 / n2
    return r
