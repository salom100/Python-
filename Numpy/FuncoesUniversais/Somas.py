# Somas
''' 
    as funções de soma sao diferentes das de ADD pois 
    o add soma os valores de cada parametros e retorna em um vetor, porem 
    soma, realiza o somatorio de todos os valores
'''

import numpy as np

m1= np.array([1,2,3])
m2= np.array([1,2,3])

add= np.add(m1,m2)
print("np.add:",add)

soma= np.sum([m1,m2])
print("np.sum:",soma)

#Somas sobre um eixo
''' Se especificar axis=1, ele somara os valores de cada matriz
'''

somaeixo= np.sum([m1,m2], axis=1)
print("np.sum(axis=1):",somaeixo)

#soma cumulativa

matriz = np.array([1,2,3])

comulativa = np.cumsum(matriz)

print("Soma cumulativa:",comulativa)
