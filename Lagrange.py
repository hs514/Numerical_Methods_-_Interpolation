import numpy as np

def lagrange(x, y, p): #onde x são os pontos, y = f(x) e p é uma lista de ponto(s) onde se quer saber f(p)
    aux = np.zeros((len(p), y.size))

    for i in range(0,len(p)):
        for k in range(y.size):
            xi, xj = x[k], np.delete(x, k)
            aux[i][k] = np.prod((p[i] - xj)/(xi - xj))

    return [sum(y*aux[i]) for i in range(len(p))]
