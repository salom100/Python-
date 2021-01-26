import numpy as np 

n = 4
n1 = 6

mmc= np.lcm(n,n1)
print(mmc)

#MMC em uma matriz np.lcm.reduce()
m = np.array([3,6,9])

matrizmmc= np.lcm.reduce(m)
print(matrizmmc)

matriz = np.arange(1,11)

MMC = np.lcm.reduce(matriz)

print(MMC)