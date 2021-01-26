import numpy as np

#A COPIA CRIA UMA NOVA MATRIZ 
# e as alterações no original e na copiam nao afetam a outra matriz
# as copias possuem os dados

matriz = np.array([1,2,3,4,5])

copia = matriz.copy()
matriz[0]=42 # alteração no original

print("ORIGINAL: ",matriz)
print("COPIA: ",copia)


#A VISAO SO REPLICA A MATRIZ ORIGINAL
# As laterações em ambas matrizes afetam uma na outra
# as visoes nao possuem os dados

matriz2 = np.array([1,2,3,4,5])

visao = matriz2.view()
matriz2[0] = 450 #alteração na matriz original

visao[0] = 20

print("Original: ",matriz2)
print("visao: ",visao)


# DESCOBRINDO SE A matriz possui os valores
# retorna none se possui os dados, se nao possuir ele retorna a matriz original
arr = np.array([1,2,3,4,5])

a = arr.copy()
b = arr.view()

print(a.base)
print(b.base)