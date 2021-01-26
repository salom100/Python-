import numpy as np 
from numpy import random

#USANDO O SHUFFLE
# ele altera a matriz original
matriz = np.array([1,2,3,4,5])

random.shuffle(matriz)

print(matriz)

#USANDO O PERMUTATION
# ele nao afeta na matriz original

m = np.array([1,2,3,4,5])
random.permutation(m)
print(m)
