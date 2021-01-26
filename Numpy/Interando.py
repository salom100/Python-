import numpy as np 

matriz = np.array([1,2,3])

for x in matriz:
    print(x)

matriz2D = np.array([[1,2,3],[4,5,6]])

for x in matriz2D:
    print(x)

for x in matriz2D:
    for y in x:
        print(y)

matriz3D = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

for x in matriz3D:
    print(x)

for x in matriz3D:
    for y in x:
        for z in y:
            print(z)

# ITERANDO MATRIZ COM nditer()
A = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])

for x in np.nditer(A):
    print(x)

# Iterando e mudando o tipo com nditer()
matrizint = np.array([1,2,3])

for x in np.nditer(matrizint, flags=["buffered"], op_dtypes=['S']):
    print(x)

M2D = np.array([[1,2,3,4],[5,6,7,8]])

#correndo a matriz e indo de 2 em 2
for i in np.nditer(M2D[:, ::2]):
    print(i)


# ndnumerate()
arr = np.array([1,2,3])

print("enumerando matriz 1D")
for idx, x in np.ndenumerate(arr):
    print(idx,x)

#enumerando uma matriz 2d
print("enumerando uma matriz 2d")
for idx, x in np.ndenumerate(M2D):
    print(idx,x)





















