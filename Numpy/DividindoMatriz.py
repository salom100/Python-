import numpy as np

A = np.array([1,2,3,4,5,6])

print("Matriz Original")
print(A)

#array_split(Matriz,Divisoes)
# existe tambem o split() porem ele nao se ajusta no caso de uma divisao irregular
print("Matriz divida por 3")
AD3 = np.array_split(A,3)

print(AD3)

print("Matriz dividida por 4")
AD4 = np.array_split(A,4)
print(AD4)

# É possivel acessar os valores divididos atraves do indice
print(AD4[0])
print(AD4[2])


# DIVIDINDO MATRIZES 2D
Matriz2D = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
print("\n\nDIVIDINDO MATRIZ 2D EM 3")
divisao2D = np.array_split(Matriz2D,3)
print(divisao2D)

print("\n\nDIVIDINDO MATRIZ 2D grande EM 3")
M2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
div2D = np.array_split(M2D,3)
print(div2D)

#dividindo com o eixo = 1
print("\n\nDividindo Matriz 2D em 3 com o eixo=1")
D2D = np.array_split(M2D, 3, axis= 1) 
print(D2D)

#dividindo usando o hsplit() = divide com base na linhas
Dh2D = np.hsplit(M2D,3)
print(Dh2D)

#NOTA: assim como usamos o vstack() e dstack() é possivel usar o vsplit() e dsplit()