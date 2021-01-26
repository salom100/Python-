#Classificando Matriz
# Classificar significa ordenar

import numpy as np 


#np.sort() pode organizar desde numeros ate strings em ordem
matriz = np.array([1,0,3,2])
print(np.sort(matriz))

frutas = np.array(["Morango","Abacaxi","Banana"])
print(np.sort(frutas))

Mboolean = np.array([True, False, True])
print(np.sort(Mboolean))

#classificando uma matriz 2d
Matriz2D = np.array([[3,1,2], [6,4,5]])
print(np.sort(Matriz2D))

