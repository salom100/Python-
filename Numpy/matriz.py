import numpy as np

#Matrizes 0-D
arr = np.array(42)

print(arr)

#Matrizes 1-D
matriz1D= np.array([1,2,3,4,5])

print(matriz1D)

#Matrizes 2-D
matriz2D= np.array([[1,2,3],[4,5,6]])

print(matriz2D)

#Matriz 3-D
matriz3D= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
                

print(matriz3D)


# VERIFICAR O NUMERO DE DIMENSÕES
print("NUMERO DE DIMENSOES das matrizes")

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Definir o numero de dimensões da matriz
matrizND = np.array([1,2,3,4,5], ndmin= 5)

print(matrizND)
print("numero de dimensoes: ", matrizND.ndim)