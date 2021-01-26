'''
Em SQL, unimos tabelas com base em uma chave, 
    enquanto em NumPy unimos arrays por eixos.

Usamos concatenate() 
    se o eixo nao for passado, ele é considerado 0
'''

import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])

print("matriz 1")
print(A)

print("matriz 2")
print(B)

AB = np.concatenate((A,B))

print("junção das matrizes")
print(AB)

# JUNTANDO MATRIZ 2Ds
A2D = np.array([[1,2], [3,4]])
B2D = np.array([[5,6], [7,8]])

AB2D = np.concatenate((A2D,B2D), axis=1)
print("junção com contatenate numa matriz 2D")
print(AB2D)

#usando pilha para fazer junção
pilha = np.stack((A2D,B2D), axis=1)
print("Juncao com pilha")
print(pilha)

# usando hstack() para fazer a junção por linhas
EL = np.hstack((A2D,B2D))
print("Junção usando empilhamento por linha")
print(EL)

# usando o vstack() para fazer a junção por colunas
EC = np.vstack((A2D,B2D))
print("Junção usando empilhamento por colunas")
print(EC)

# empilhamento ao longo da profundidade
EP = np.dstack((A2D,B2D))
print("Juncao usando empilhamento por profundidade")
print(EP)
