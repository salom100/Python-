#PESQUISANDO EM MATRIZ
import numpy as np 


M = np.array([1,2,3,4,5,4,4])

print(M)
busca = np.where(M == 4)

print("O numero 4 se encontra no indice: ",busca)

#Buscando os valores pares na matriz
M1 = np.array([1,2,3,4,5,6,7,8])
par= np.where(M1%2 == 0)

impar = np.where(M1%2 == 1)
print(M1)
print("Indices aonde os valores sao pares",par)
print("Indices aonde os valores sao impares",impar)

#PESQUISA ORDENADA
#np.searchsorted(matriz, valor)

M2 = np.array([6,7,8,9])

pesquisa = np.searchsorted(M2,7)

print(pesquisa)

pesquisaLadoDireito = np.searchsorted(M2, 7 , side="right")
print(pesquisaLadoDireito)

#Valores multiplos organizados
M3 = np.array([1,3,5,7])

p = np.searchsorted(M3, [2,4,6])
print(p)
#O valor de retorno é um array: [1 2 3]contendo os 
# três índices onde 2, 4, 6 seriam inseridos no array 
# original para manter a ordem.

