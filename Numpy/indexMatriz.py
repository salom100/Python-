import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[0])

print(arr[4])

print(arr[1] + arr[3])

#MATRIZ 2-D 
matriz2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("Segundo elemento da primeira dimensão:", matriz2D[0,1])

print("5º Elemento da segunda dimensão:", matriz2D[1,4])

print("Ultimo elemento da segunda dimensão: ", matriz2D[1,-1])

#MATRIZ 3-D
matriz3D= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

#terceiro elemento da segunda matriz da primeira matriz
print("terceiro elemento da segunda matriz da primeira matriz:", matriz3D[0,1,2])

