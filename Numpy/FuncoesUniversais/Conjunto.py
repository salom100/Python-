'''
    Um conjunto em matemática é uma coleção de elementos únicos.

Os conjuntos são usados ​​para operações que envolvem operações frequentes de intersecção, união e diferença.
'''
import numpy as np

m = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

unicos = np.unique(m)
print(unicos)

#Unindo duas matrizes com valores unicos
m1 = np.array([1,2,3,4])
m2 = np.array([3,4,5,6])

uniao = np.union1d(m1,m2)
print(uniao)

# Achando cruzamento (intersecção)

#assume_unique=True -pode acelerar o calculo
inter = np.intersect1d(m1,m2, assume_unique=True)
print(inter)

# Encontrando a diferença
diff = np.setdiff1d(m1,m2, assume_unique=True)
print(diff)


# Encontrando diferença simetrica
diffSimetrica = np.setxor1d(m1,m2, assume_unique=True)
print(diffSimetrica)