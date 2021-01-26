#https://www.w3schools.com/python/numpy_array_slicing.asp

import numpy as np 

matriz = np.array([1,2,3,4,5,6,7])

#capta os valores de um determinado espaço [inicio:fim]
#O resultado inclui o índice inicial, mas exclui o índice final.
print(matriz[1:5])

print(matriz[4:])

print(matriz[:4])

print(matriz[-3:-1])

# mostra no intervalo de quantos em quantos
print(matriz[1:5:2])

print(matriz[::2])

#FATIAMENTO DE MATRIZ 2-D
matriz2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#A partir do segundo elemento, divida os elementos do índice 1 ao índice 4 (não incluído)
print(matriz2D[1,1:4])

#retorna o segundo indice das duas dimensões
print(matriz2D[0:2, 2])

print(matriz2D[0:2 , 1:4])


#retorna o tipo da matriz
print(matriz2D.dtype)

Frutas = np.array(["Maça","Laranja","Pessego"])
print(Frutas.dtype)


#DEFININDO O TIPO DA MATRIZ (OPCIONAL)
matrizstring = np.array([1,2,3,4,5], dtype = "S")
print(matrizstring)
print(matrizstring.dtype)

# dos tipos : i, u, f, S e U é possivel definir o tamanho
tamanho = np.array([1,2,3,4,5], dtype="i4")
print(tamanho)
print(tamanho.dtype)


#CONVERTENDO O TIPO DE DADOS COM O ASTYPE

matrizfloat = np.array([1.1,1.2,1.3])

# matrizint= matrizfloat.astype('i')
matrizint= matrizfloat.astype(int)

print(matrizint)
print(matrizint.dtype)

# Convertendo para booleano
A = np.array([1,0,3])

Aboolean = A.astype(bool)

print(Aboolean)
print(Aboolean.dtype)
