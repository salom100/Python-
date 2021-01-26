#Funções de aritmetica simples

import numpy as np 

matriz1 = np.array([5,10,15,20,25,30])
matriz2 = np.array([10,20,30,40,50,60])



print("Matrizes originais")
print("Matriz 1: ",matriz1)
print("Matriz 2: ",matriz2)

print("\n\nFunções universais:")
soma = np.add(matriz1, matriz2)
print("Soma: ",soma)
subtrai= np.subtract(matriz1,matriz2)
print("Subtração: ",subtrai)
multi = np.multiply(matriz1,matriz2)
print("Multiplicação: ",multi)
div= np.divide(matriz1, matriz2)
print("Divisao: ",div)
eleva= np.power(matriz1,matriz2)
print("Elevação: ",eleva)
restante = np.mod(matriz1,matriz2)
print("Restante(mod): ",restante)
restante2= np.remainder(matriz1, matriz2)
print("Restante(remainder): ",restante2)
QuocienteMod= np.divmod(matriz1,matriz2)
print("QuocienteMod: ",QuocienteMod)
ValoresAbsolutos = np.absolute(matriz1,matriz2)
print("Valores Absolutos:",ValoresAbsolutos)










