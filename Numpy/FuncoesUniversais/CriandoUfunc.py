# Podemos criar uma ufunc
'''
    para se criar uma ufunc necessitamos usar o metodo frompyfunc()

    possui 3 argumentos:
    function = nome da função
    inputs = o numero de argumentos de entrada(matrizes)
    outputs= numero de matrizes de saida
'''

import numpy as np 

def minhaSoma(x,y):
    return x+y

soma = np.frompyfunc(minhaSoma, 2,1)

print(soma([1,2,3,4],[5,6,7,8]))

#Verificando se uma função é universal
print(type(np.add))
print(type(np.concatenate))

if type(np.add) == np.ufunc:
    print("add é uma função universal")
else:
    print("add nao é uma função universal")