import numpy as np 

matriz = np.array([[1,2,3,4],[5,6,7,8]])

# retorna uma tupla informando quantas:
#dimensões possui e quantos elementos possui
print(matriz.shape)


matriz5 = np.array([1,2,3,4], ndmin = 5)

print(matriz5)
print("FORMA DA MATRIZ: \n",matriz5.shape)

#REMODELANDO matriz
# ela retorna visualizações e nao copias

# matriz 1-D para 2-D e 3-D
matriz1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("MATRIZ 1-D")
print(matriz1D)

matriz2D = matriz1D.reshape(4,3)

print("Transformando para Matriz 2-D")
print(matriz2D)


matriz3D= matriz1D.reshape(2,3,2)
print("Transformando para Matriz 3D")

print(matriz3D)

#DIMENSAO DESCONHECIDA
print("DIMENSAO DESCONHECIDA")

M = np.array([1,2,3,4,5,6,7,8])
MD = M.reshape(2,2,-1)
print(MD)

#ACHATANDO MATRIZES
M2 = np.array([[1,2,3],[4,5,6]])
M1 = M2.reshape(-1)

print("ACHATANDO MATRIZ")
print(M1)
