import numpy as np 

m = np.array([1,2,3,4,5])

produto = np.prod(m)

print(produto)

m1 = np.array([1,2,3,4])
m2 = np.array([5,6,7,8])

prod = np.prod([m1,m2])
print(prod)

prodEixo= np.prod([m1,m2], axis=1)
print("Prod de cada matriz:",prodEixo)

#Produto Comulativo
matriz = np.array([5,10,15,20])

prodC= np.cumprod(matriz)

print(prodC)