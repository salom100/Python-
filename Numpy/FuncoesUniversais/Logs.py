import numpy as np
from math import log

matriz = np.arange(1,10)

print(matriz)
print("\n np.log2(matriz):")
print(np.log2(matriz))

print("\n np.log10(matriz):")
print(np.log10(matriz))

print("\n registro natural")
print(np.log(matriz))

#Log em qualquer base
nplog = np.frompyfunc(log,2,1)

print("\n Log em qualquer base")
print(nplog(100,15))
