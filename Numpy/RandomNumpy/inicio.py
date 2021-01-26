from numpy import random

#aleatorio entre 0 e 100 
x = random.randint(100)

#aleatorio entre 0 a 1
y = random.rand()

print(x)
print(y)

#GERANDO MATRIZ ALEATORIA

#gera matriz de tamanho 5
matriz = random.randint(100, size=5)
print("\n\nmatriz aleatoria de tamanho 5 ")
print(matriz)

matriz2D = random.randint(100, size=(3,5))
print("\n\nMatriz aleatoria de 3 linhas e 5 colunas")
print(matriz2D)

#matriz  aleatoria com valores float
matrizF = random.rand(5)
print("\n\nMatriz aleatoria (Floats)")
print(matrizF)

#matriz 2 D aleatoria com valores float
matriz2DF = random.rand(3,5)
print("\n\nmatriz 2 D aleatoria (floats)")
print(matriz2DF)


#Gerando valores aleatorios se baseando em uma matriz

#random.choice([valores]) aleatoriamente escolhe um dos valores 
M = random.choice([3,5,7,9])
print("\n\nValores aleatorios pre definidos entre [3,5,7,9]")
print(M)

M2 = random.choice([3,5,7,9], size=(3,5))

print("\n\nMatriz 2 D com valores escolhidos aleatoriamente [3,5,7,9]")
print(M2)