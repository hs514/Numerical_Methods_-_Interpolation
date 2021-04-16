import numpy as np

def estimativa_erro(x,y,p): #onde x são os pontos, y = f(x) e p é uma lista de ponto(s) onde se quer saber a estimativa de erro para f(p)
    M = diferencas_divididas(x,y)[0,1:]
    n = len(x)-1

    aux = [np.prod(p[i] - x[0:n]) for i in range(0,len(p))]

    return [abs(aux[i])*abs(M[n-1]) for i in range(0,len(p))] #estimativa ddo erro de f(p)

def diferencas_divididas(x, y): #onde x são os pontos e y são os f(x)
    n = len(x)
    M = np.zeros((n,n+1))
    
    M[:,0], M[:,1] = x, y
    
    for i in range(2,n+1): #colunas
        for j in range(0,(n+1)-i): #linhas
            M[j,i] = (M[j+1,i-1] - M[j,i-1])/(M[(i-1)+j,0] - M[j,0])
    
    return M[:,1:] #Cada coluna é uma ordem de mesmo índice, que determina a ordem do polinômio que poderá ser gerado

def newton_interpolador(x, y, p): #onde x são os pontos, y = f(x) e p é uma lista de ponto(s) onde se quer saber f(p)
    M = diferencas_divididas(x,y)[0,1:]
    n = len(x)-1

    aux = np.zeros(len(p))
    for j in range(0,len(p)):
        for i in range(0,n):
            aux[j] += np.prod(p[j] - x[0:i+1]) * M[i]
    
    return y[0] + aux #f(p)
