from numpy import random

#definindo a provabilidade do numero ser escolhido
#A soma de todos os números de probabilidade deve ser 1.

matriz = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
print("Matriz 1 D contendo valores aleatorios ate 100")
print(matriz)


matriz2D = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5))
print("\n\nMatriz 2 D contendo valores aleatorios e probabilidades definidas")
print(matriz2D)