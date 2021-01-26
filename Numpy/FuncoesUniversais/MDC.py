import numpy as np

n= 5
n1 = 20

mdc = np.gcd(n,n1)

print(mdc)

matriz= np.array([28,8,32,36,16])

MDCmatriz= np.gcd.reduce(matriz)
print(MDCmatriz)